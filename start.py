from main import build_app

if __name__ == "__main__":
    app = build_app()
    print("🤖 Bot is starting...")
    app.run_polling()
