import asyncio
from main import build_app

async def main():
    print("🤖 Bot is starting...")
    app = build_app()
    await app.initialize()
    await app.start()
    await app.bot.initialize()
    await app.updater.start_polling()
    await asyncio.Event().wait()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
