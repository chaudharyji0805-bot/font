from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN, FORCE_CHANNELS

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
    buttons = []
    for ch in FORCE_CHANNELS:
        buttons.append([InlineKeyboardButton(f"Join {ch}", url=f"https://t.me/{ch.lstrip('@')}")])

    buttons.append([InlineKeyboardButton("✅ Joined, Retry", callback_data="retry_join")])

    msg = (
        "🚫 Bhai pehle in channels ko join kar:\n\n"
        "👉 Join karne ke baad **Joined, Retry** pe click kar.\n\n"
        "Phir bot use kar paayega 😎"
    )

    if update.message:
        await update.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(buttons), parse_mode="Markdown")

# ---- /start command ----
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

# ---- Text handler (SAFE + Force Join check) ----
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    if not await is_user_joined(update, context):
        await send_force_join(update, context)
        return

    text = update.message.text
    reply = f"✨ Tera text mil gaya:\n{text}"
    await update.message.reply_text(reply)

# ---- Callback for "Joined, Retry" ----
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not await is_user_joined(update, context):
        await query.edit_message_text("❌ Abhi bhi join nahi kiya bhai. Pehle join kar phir retry kar.")
        await send_force_join(update, context)
        return

    await query.edit_message_text("✅ Verified! Ab bot use kar sakta hai.\n\n✍️ Ab koi text bhej.")

def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    app.add_handler(MessageHandler(filters.StatusUpdate.ALL, lambda u, c: None))
    app.add_handler(MessageHandler(filters.ALL, lambda u, c: None))
    app.add_handler(CommandHandler("retry", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("about", start))

    from telegram.ext import CallbackQueryHandler
    app.add_handler(CallbackQueryHandler(handle_callback))

    return app
