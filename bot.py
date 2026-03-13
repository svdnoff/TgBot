from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN ="8632066324:AAHTAri1Owiv_T7-OfebMF9vFsBhQxDOFmU"

ADDRESS_TEXT = "📍 Наш адрес: Майкоп, ул. Строителей 8Б (район железного рынка)"
WORK_TIME = "🕒 Мы работаем: 10:00–19:00 каждый день, кроме понедельника"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "адрес" in text or "где найти" in text or "где приехать" in text or "где вы" in text or "где находитесь" in text or "как найти" in text:
        await update.message.reply_text(
            ADDRESS_TEXT,
            reply_to_message_id=update.message.message_id
        )

    elif "время работы" in text or "работаете" in text or "до скольки" or "рабочий день" in text or "график работы" in text:
        await update.message.reply_text(
            WORK_TIME,
            reply_to_message_id=update.message.message_id
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()