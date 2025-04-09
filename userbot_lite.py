from pyrogram import Client, filters

api_id = 123456  # Replace with your API ID
api_hash = "your_api_hash"  # Replace with your API Hash

app = Client("userbot_lite", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(_, msg):
    await msg.reply("🏓 Pong!")

@app.on_message(filters.command("help", prefixes=".") & filters.me)
async def help_cmd(_, msg):
    text = (
        "📖 Available commands:\n"
        ".ping – Check if the bot is alive\n"
        ".listproducts – Show a list of demo products\n\n"
        "🔐 Want the full version with PayPal, broadcasting, and more?\n"
        "📩 Contact us: @plasmonplus"
    )
    await msg.reply(text)

@app.on_message(filters.command("listproducts", prefixes=".") & filters.me)
async def listproducts(_, msg):
    products = [
        "💼 Product 1 – Demo description",
        "📦 Product 2 – Demo description",
        "🎁 Product 3 – Demo description"
    ]
    await msg.reply("\n".join(products))

@app.on_message(filters.command("start", prefixes=".") & filters.me)
async def start_notice(_, msg):
    await msg.reply(
        "✨ Welcome to UserBotShop Lite!\n"
        "Use .help to see available commands.\n\n"
        "📩 For the full PRO version → @plasmonplus"
    )

app.run()
