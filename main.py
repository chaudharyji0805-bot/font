import sqlite3
from uuid import uuid4
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    InlineQueryResultArticle, InputTextMessageContent
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    CallbackQueryHandler, InlineQueryHandler, ContextTypes, filters
)
from config import BOT_TOKEN, FORCE_CHANNELS, ADMINS, WATERMARK

# ================== DATABASE ==================
conn = sqlite3.connect("bot.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    fav_style INTEGER DEFAULT 0
)
""")
conn.commit()

def add_user(user_id: int):
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()

def set_fav(user_id: int, idx: int):
    add_user(user_id)
    cur.execute("UPDATE users SET fav_style=? WHERE user_id=?", (idx, user_id))
    conn.commit()

def get_fav(user_id: int):
    add_user(user_id)
    cur.execute("SELECT fav_style FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    return row[0] if row else 0

def total_users():
    cur.execute("SELECT COUNT(*) FROM users")
    return cur.fetchone()[0]

# ================== FONTS ==================
def map_chars(text, base):
    out = ""
    for c in text:
        if "a" <= c <= "z":
            out += chr(ord(c) - 97 + base)
        elif "A" <= c <= "Z":
            out += chr(ord(c) - 65 + base - 26)
        else:
            out += c
    return out

CATEGORIES = {
    "Simple": [
        ("Normal", lambda t: t),
        ("Wide", lambda t: " ".join(list(t))),
        ("Reverse", lambda t: t[::-1]),
    ],
    "Fancy": [
        ("Bold", lambda t: map_chars(t, 0x1D400)),
        ("Italic", lambda t: map_chars(t, 0x1D434)),
        ("Bold Italic", lambda t: map_chars(t, 0x1D468)),
        ("Monospace", lambda t: map_chars(t, 0x1D670)),
    ],
    "Symbols": [
        ("Bubble", lambda t: "".join(f"{c}⃝" if c.isalnum() else c for c in t)),
        ("Strike", lambda t: "".join(c + "̶" if c != " " else c for c in t)),
        ("Underline", lambda t: "".join(c + "̲" if c != " " else c for c in t)),
    ],
    "Fun": [
        ("Dots", lambda t: "•".join(list(t))),
        ("Hearts", lambda t: "❤".join(list(t))),
        ("Leet", lambda t: t.replace("a","4").replace("e","3").replace("i","1").replace("o","0")),
    ]
}

FONTS = []
for cat, items in CATEGORIES.items():
    for name, fn in items:
        FONTS.append((f"{cat} - {name}", fn))

# ================== STATE ==================
USER_STATE = {}  # user_id: {"text": str, "idx": int}

# ================== FORCE JOIN ==================
async def is_user_joined(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    user_id = update.effective_user.id
    bot = context.bot
    for ch in FORCE_CHANNELS:
        try:
            member = await bot.get_chat_member(chat_id=ch, user_id=user_id)
            if member.status in ("left", "kicked"):
                return False
        except Exception:
            return False
    return True

async def send_force_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch.lstrip('@')}")] for ch in FORCE_CHANNELS]
    buttons.append([InlineKeyboardButton("✅ Joined, Retry", callback_data="retry_join")])
    msg = "🚫 Bhai pehle channels join kar:\n\nJoin karke **Joined, Retry** dabaa 😎"
    markup = InlineKeyboardMarkup(buttons)
    if update.message:
        await update.message.reply_text(msg, reply_markup=markup)
    elif update.callback_query:
        await update.callback_query.message.reply_text(msg, reply_markup=markup)

# ================== RENDER ==================
def render_text(user_id: int):
    state = USER_STATE[user_id]
    text = state["text"]
    idx = state["idx"] % len(FONTS)
    name, fn = FONTS[idx]
    try:
        styled = fn(text)
    except Exception:
        styled = text
    return f"✨ Style: {name}\n\n{styled}{WATERMARK}"

def nav_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⬅️ Prev", callback_data="prev"),
            InlineKeyboardButton("➡️ Next", callback_data="next"),
        ],
        [
            InlineKeyboardButton("⭐ Save", callback_data="save"),
            InlineKeyboardButton("📋 Copy", callback_data="copy"),
        ]
    ])

# ================== COMMANDS ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return

    user_id = update.effective_user.id
    add_user(user_id)

    fav = get_fav(user_id)
    msg = "🔥 Welcome bhai!\n\n✍️ Text bhej, main stylish bana dunga."
    msg += f"\n⭐ Tera saved style: {FONTS[fav][0]}"
    await update.message.reply_text(msg)

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    total = total_users()
    await update.message.reply_text(f"📊 Bot Stats:\n\n👥 Total Users: {total}")

# ================== TEXT HANDLER ==================
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return

    user_id = update.effective_user.id
    add_user(user_id)

    start_idx = get_fav(user_id)
    USER_STATE[user_id] = {"text": update.message.text, "idx": start_idx}

    out = render_text(user_id)
    await update.message.reply_text(out, reply_markup=nav_keyboard())

# ================== CALLBACK ==================
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "retry_join":
        if not await is_user_joined(update, context):
            await query.edit_message_text("❌ Pehle join kar bhai.")
            await send_force_join(update, context)
            return
        await query.edit_message_text("✅ Verified! Ab text bhej.")
        return

    if user_id not in USER_STATE:
        await query.edit_message_text("✍️ Pehle koi text bhejo bhai.")
        return

    if query.data == "next":
        USER_STATE[user_id]["idx"] += 1
    elif query.data == "prev":
        USER_STATE[user_id]["idx"] -= 1
    elif query.data == "save":
        idx = USER_STATE[user_id]["idx"] % len(FONTS)
        set_fav(user_id, idx)
        await query.answer("⭐ Style saved!", show_alert=True)
    elif query.data == "copy":
        out = render_text(user_id)
        await query.message.reply_text(out)
        return

    out = render_text(user_id)
    await query.edit_message_text(out, reply_markup=nav_keyboard())

# ================== INLINE MODE ==================
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return

    results = []
    for name, fn in FONTS[:12]:
        try:
            styled = fn(query)
        except Exception:
            styled = query

        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=name,
                input_message_content=InputTextMessageContent(styled + WATERMARK),
                description=styled[:50]
            )
        )

    await update.inline_query.answer(results, cache_time=1)

# ================== ADMIN BROADCAST ==================
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMINS:
        await update.message.reply_text("❌ Tu admin nahi hai bhai.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /broadcast message")
        return

    msg = " ".join(context.args)
    sent = 0

    cur.execute("SELECT user_id FROM users")
    rows = cur.fetchall()
    for (uid,) in rows:
        try:
            await context.bot.send_message(chat_id=uid, text=msg)
            sent += 1
        except Exception:
            pass

    await update.message.reply_text(f"✅ Broadcast sent to {sent} users.")

# ================== BUILD APP ==================
def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(InlineQueryHandler(inline_query))
    return app
