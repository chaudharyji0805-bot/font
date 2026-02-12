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
from config import BOT_TOKEN, FORCE_CHANNELS, ADMINS
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

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

# ================== FONT HELPERS ==================
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

def small_caps(t):
    table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ"
    )
    return t.translate(table)

def bubble(t):
    return "".join(f"{c}⃝" if c.isalnum() else c for c in t)

def strike(t):
    return "".join(c + "̶" if c != " " else c for c in t)

def underline(t):
    return "".join(c + "̲" if c != " " else c for c in t)

def hearts(t):
    return "❤".join(list(t))

def dots(t):
    return "•".join(list(t))

def leet(t):
    return t.replace("a","4").replace("e","3").replace("i","1").replace("o","0").replace("s","5").replace("t","7")

# ================== 50+ FONTS ==================
FONTS = [
    ("Normal", lambda t: t),
    ("Wide", lambda t: " ".join(list(t))),
    ("Reverse", lambda t: t[::-1]),
    ("Upper", lambda t: t.upper()),
    ("Lower", lambda t: t.lower()),
    ("Small Caps", small_caps),
    ("Leet", leet),

    ("Bold", lambda t: map_chars(t, 0x1D400)),
    ("Italic", lambda t: map_chars(t, 0x1D434)),
    ("Bold Italic", lambda t: map_chars(t, 0x1D468)),
    ("Script", lambda t: map_chars(t, 0x1D49C)),
    ("Bold Script", lambda t: map_chars(t, 0x1D4D0)),
    ("Fraktur", lambda t: map_chars(t, 0x1D504)),
    ("Double Struck", lambda t: map_chars(t, 0x1D538)),
    ("Sans", lambda t: map_chars(t, 0x1D5A0)),
    ("Sans Bold", lambda t: map_chars(t, 0x1D5D4)),
    ("Sans Italic", lambda t: map_chars(t, 0x1D608)),
    ("Sans Bold Italic", lambda t: map_chars(t, 0x1D63C)),
    ("Monospace", lambda t: map_chars(t, 0x1D670)),

    ("Bubble", bubble),
    ("Strike", strike),
    ("Underline", underline),
    ("Hearts", hearts),
    ("Dots", dots),
    ("Star", lambda t: "★".join(list(t))),
    ("Fire", lambda t: "🔥".join(list(t))),
    ("Cool Box", lambda t: f"『{t}』"),
    ("Brackets", lambda t: f"[ {t} ]"),
    ("Curly", lambda t: f"{{ {t} }}"),
    ("Angle", lambda t: f"⟨ {t} ⟩"),
    ("Wave", lambda t: "～".join(list(t))),
    ("Arrow", lambda t: "➤".join(list(t))),
    ("X Style", lambda t: "✖".join(list(t))),
    ("Circle", lambda t: "○".join(list(t))),
    ("Diamond", lambda t: "◆".join(list(t))),
    ("Square", lambda t: "■".join(list(t))),
    ("Heart Box", lambda t: f"❤️ {t} ❤️"),
    ("Cool Line", lambda t: f"— {t} —"),

    ("Crazy 1", lambda t: hearts(bubble(t))),
    ("Crazy 2", lambda t: dots(strike(t))),
    ("Crazy 3", lambda t: bubble(leet(t))),
    ("Crazy 4", lambda t: underline(hearts(t))),
    ("Crazy 5", lambda t: strike(dots(t))),
    ("Crazy 6", lambda t: f"🔥 {bubble(t)} 🔥"),
    ("Crazy 7", lambda t: f"★ {map_chars(t,0x1D400)} ★"),
    ("Crazy 8", lambda t: f"『{hearts(t)}』"),
    ("Crazy 9", lambda t: f"⟦ {small_caps(t)} ⟧"),
    ("Crazy 10", lambda t: f"✦ {dots(t)} ✦"),
]

# ================== STATE ==================
USER_STATE = {}

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
    markup = InlineKeyboardMarkup(buttons)
    msg = "🚫 Bhai pehle channels join kar 😎"
    if update.message:
        await update.message.reply_text(msg, reply_markup=markup)
    else:
        await update.callback_query.message.reply_text(msg, reply_markup=markup)

# ================== RENDER ==================
def render_text(user_id: int):
    state = USER_STATE[user_id]
    text = state["text"]
    idx = state["idx"] % len(FONTS)
    name, fn = FONTS[idx]
    try:
        styled = fn(text)
    except:
        styled = text
    return f"✨ Style: {name}\n\n{styled}"

def nav_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("⬅️ Prev", callback_data="prev"), InlineKeyboardButton("➡️ Next", callback_data="next")],
        [InlineKeyboardButton("⭐ Save", callback_data="save"), InlineKeyboardButton("📋 Copy", callback_data="copy")]
    ])

# ================== COMMANDS ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return
    user_id = update.effective_user.id
    add_user(user_id)
    fav = get_fav(user_id)
    await update.message.reply_text(f"🔥 Welcome bhai!\n✍️ Text bhej.\n⭐ Saved style: {FONTS[fav][0]}")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🤖 *Tujsebot Help*\n\n"
        "• Text bhejo → Stylish banega\n"
        "• ⬅️➡️ se style badlo\n"
        "• ⭐ Save → favorite save\n"
        "• 📋 Copy → text copy\n\n"
        "Commands:\n"
        "/start\n/help\n/stats\n\n"
        "Inline:\n`@Tujsebot hello`"
    )
    await update.message.reply_text(text, parse_mode="Markdown")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"👥 Total Users: {total_users()}")

# ================== TEXT ==================
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return
    user_id = update.effective_user.id
    add_user(user_id)
    USER_STATE[user_id] = {"text": update.message.text, "idx": get_fav(user_id)}
    await update.message.reply_text(render_text(user_id), reply_markup=nav_keyboard())

# ================== CALLBACK ==================
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    user_id = q.from_user.id

    if q.data == "retry_join":
        if not await is_user_joined(update, context):
            await send_force_join(update, context)
        else:
            await q.edit_message_text("✅ Verified! Ab text bhej.")
        return

    if user_id not in USER_STATE:
        await q.edit_message_text("✍️ Pehle text bhejo.")
        return

    if q.data == "next":
        USER_STATE[user_id]["idx"] += 1
    elif q.data == "prev":
        USER_STATE[user_id]["idx"] -= 1
    elif q.data == "save":
        set_fav(user_id, USER_STATE[user_id]["idx"] % len(FONTS))
        await q.answer("⭐ Saved!", show_alert=True)
    elif q.data == "copy":
        await q.message.reply_text(render_text(user_id))
        return

    await q.edit_message_text(render_text(user_id), reply_markup=nav_keyboard())

# ================== INLINE ==================
async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = []
    for name, fn in FONTS[:20]:
        try:
            styled = fn(query)
        except:
            styled = query
        results.append(
            InlineQueryResultArticle(
                id=str(uuid4()),
                title=name,
                input_message_content=InputTextMessageContent(styled),
                description=styled[:50]
            )
        )
    await update.inline_query.answer(results, cache_time=1)

# ================== BROADCAST ==================
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in ADMINS:
        await update.message.reply_text("❌ Admin only.")
        return
    msg = " ".join(context.args)
    sent = 0
    cur.execute("SELECT user_id FROM users")
    for (uid,) in cur.fetchall():
        try:
            await context.bot.send_message(uid, msg)
            sent += 1
        except:
            pass
    await update.message.reply_text(f"✅ Sent to {sent} users.")

# ================== APP ==================
def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(InlineQueryHandler(inline_query))
    return app

if __name__ == "__main__":
    app = build_app()
    app.run_polling()
