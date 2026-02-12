from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from config import BOT_TOKEN, FORCE_CHANNELS, ADMINS, WATERMARK

# ---- 20+ Stylish Fonts ----
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

FONTS = [
    ("Normal", lambda t: t),
    ("Bold", lambda t: map_chars(t, 0x1D400)),
    ("Italic", lambda t: map_chars(t, 0x1D434)),
    ("Bold Italic", lambda t: map_chars(t, 0x1D468)),
    ("Monospace", lambda t: map_chars(t, 0x1D670)),
    ("Script", lambda t: map_chars(t, 0x1D49C)),
    ("Fraktur", lambda t: map_chars(t, 0x1D504)),
    ("Double", lambda t: map_chars(t, 0x1D538)),
    ("Sans", lambda t: map_chars(t, 0x1D5A0)),
    ("Sans Bold", lambda t: map_chars(t, 0x1D5D4)),
    ("Sans Italic", lambda t: map_chars(t, 0x1D608)),
    ("Sans BI", lambda t: map_chars(t, 0x1D63C)),
    ("SmallCaps", lambda t: t.lower()),
    ("Bubble", lambda t: "".join(f"{c}⃝" if c.isalnum() else c for c in t)),
    ("Strike", lambda t: "".join(c + "̶" if c != " " else c for c in t)),
    ("Underline", lambda t: "".join(c + "̲" if c != " " else c for c in t)),
    ("Wide", lambda t: " ".join(list(t))),
    ("Reverse", lambda t: t[::-1]),
    ("Leet", lambda t: t.replace("a","4").replace("e","3").replace("i","1").replace("o","0")),
    ("Dots", lambda t: "•".join(list(t))),
    ("Hearts", lambda t: "❤".join(list(t))),
]

# ---- In-memory DB ----
USER_STATE = {}      # user_id: {"text": str, "idx": int}
USER_FAV = {}        # user_id: idx
ALL_USERS = set()    # for broadcast

# ---- Force Join Check ----
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

# ---- Render ----
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

# ---- Commands ----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return

    user_id = update.effective_user.id
    ALL_USERS.add(user_id)

    fav = USER_FAV.get(user_id)
    msg = "🔥 Welcome bhai!\n\n✍️ Text bhej, main stylish bana dunga."
    if fav is not None:
        msg += f"\n⭐ Tera saved style: {FONTS[fav][0]}"
    await update.message.reply_text(msg)

# ---- Text Handler ----
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return

    user_id = update.effective_user.id
    ALL_USERS.add(user_id)

    start_idx = USER_FAV.get(user_id, 0)
    USER_STATE[user_id] = {"text": update.message.text, "idx": start_idx}

    out = render_text(user_id)
    await update.message.reply_text(out, reply_markup=nav_keyboard())

# ---- Callback ----
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
        USER_FAV[user_id] = USER_STATE[user_id]["idx"] % len(FONTS)
        await query.answer("⭐ Style saved!", show_alert=True)
    elif query.data == "copy":
        out = render_text(user_id)
        await query.message.reply_text(out)
        return

    out = render_text(user_id)
    await query.edit_message_text(out, reply_markup=nav_keyboard())

# ---- Admin Broadcast ----
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
    for uid in list(ALL_USERS):
        try:
            await context.bot.send_message(chat_id=uid, text=msg)
            sent += 1
        except Exception:
            pass

    await update.message.reply_text(f"✅ Broadcast sent to {sent} users.")

# ---- Build App ----
def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(handle_callback))
    return app
