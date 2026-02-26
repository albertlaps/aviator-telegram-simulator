
import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def generate_multiplier():
    r = random.random()

    if r < 0.60:
        return round(random.uniform(1.00, 2.00), 2)
    elif r < 0.85:
        return round(random.uniform(2.00, 5.00), 2)
    elif r < 0.97:
        return round(random.uniform(5.00, 15.00), 2)
    else:
        return round(random.uniform(15.00, 50.00), 2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✈️ Aviator Simulator Bot\n\nUse /play to simulate a round."
    )


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    multiplier = generate_multiplier()
    await update.message.reply_text(f"🚀 Plane flew away at: {multiplier}x")


def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN not set")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))

    print("Bot is starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
