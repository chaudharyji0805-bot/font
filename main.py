from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🔥 Welcome bhai!\n\n"
        "🤖 Ye *Font / Style Bot* hai.\n"
        "✍️ Bas apna text bhej, main usko stylish fonts me convert karke de dunga.\n\n"
        "👇 Abhi koi bhi text bhej ke try kar!"
    )
    await update.message.reply_text(msg, parse_mode="Markdown")

# Normal text handler
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # Abhi simple reply (baad me yahin font logic aayega)
    reply = f"✨ Tera text mil gaya:\n{text}\n\n(Abhi font logic add karenge 😉)"
    await update.message.reply_text(reply)

def build_app():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    return app
