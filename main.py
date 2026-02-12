from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from config import BOT_TOKEN, FORCE_CHANNELS

# ---- Simple Font Styles ----
FONTS = [
    ("Normal", lambda t: t),
    ("Bold", lambda t: "".join(chr(ord(c) + 0x1D3BF) if "a" <= c <= "z" else c for c in t)),
    ("Italic", lambda t: "".join(chr(ord(c) + 0x1D3F3) if "a" <= c <= "z" else c for c in t)),
    ("Monospace", lambda t: "".join(chr(ord(c) + 0x1D68A) if "a" <= c <= "z" else c for c in t)),
]

# ---- In-memory user state ----
USER_STATE = {}  # user_id: {"text": str, "idx": int}

# ---- Helper: check user joined all channels or not ----
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

# ---- Send Force Join Message ----
async def send_force_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [[InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch.lstrip('@')}")] for ch in FORCE_CHANNELS]
    buttons.append([InlineKeyboardButton("✅ Joined, Retry", callback_data="retry_join")])
    msg = (
        "🚫 Bhai pehle in channels ko join kar:\n\n"
        "👉 Join karne ke baad **Joined, Retry** pe click kar.\n\n"
        "Phir bot use kar paayega 😎"
    )
    markup = InlineKeyboardMarkup(buttons)
    if update.message:
        await update.message.reply_text(msg, reply_markup=markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.reply_text(msg, reply_markup=markup, parse_mode="Markdown")

# ---- /start ----
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return
    msg = (
        "🔥 Welcome bhai!\n\n"
        "🤖 Ye Font / Style Bot hai.\n"
        "✍️ Bas apna text bhej, main usko stylish bana dunga.\n\n"
        "👇 Abhi koi bhi text bhej ke try kar!"
    )
    await update.message.reply_text(msg)

# ---- Render current font ----
def render_text(user_id: int):
    state = USER_STATE[user_id]
    text = state["text"]
    idx = state["idx"] % len(FONTS)
    name, fn = FONTS[idx]
    try:
        styled = fn(text)
    except Exception:
        styled = text
    header = f"✨ Style: {name}\n\n"
    return header + styled

def nav_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⬅️ Prev", callback_data="prev"),
            InlineKeyboardButton("➡️ Next", callback_data="next"),
        ],
        [InlineKeyboardButton("📋 Copy", callback_data="copy")]
    ])

# ---- Text handler ----
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return
    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return

    user_id = update.effective_user.id
    USER_STATE[user_id] = {"text": update.message.text, "idx": 0}

    out = render_text(user_id)
    await update.message.reply_text(out, reply_markup=nav_keyboard())

# ---- Callback buttons ----
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "retry_join":
        if not await is_user_joined(update, context):
            await query.edit_message_text("❌ Abhi bhi join nahi kiya bhai. Pehle join kar phir retry kar.")
            await send_force_join(update, context)
            return
        await query.edit_message_text("✅ Verified! Ab koi text bhej.")
        return

    if user_id not in USER_STATE:
        await query.edit_message_text("✍️ Pehle koi text bhejo bhai.")
        return

    if query.data == "next":
        USER_STATE[user_id]["idx"] += 1
    elif query.data == "prev":
        USER_STATE[user_id]["idx"] -= 1
    elif query.data == "copy":
        # Telegram me direct copy button nahi hota, same text resend kar dete hain
        out = render_text(user_id)
        await query.message.reply_text(out)
        return

    out = render_text(user_id)
    await query.edit_message_text(out, reply_markup=nav_keyboard())

# ---- Build app ----
def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(CallbackQueryHandler(handle_callback))
    return app
