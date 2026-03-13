from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from rapidfuzz import fuzz

TOKEN ="8632066324:AAHTAri1Owiv_T7-OfebMF9vFsBhQxDOFmU"

ADDRESS_TEXT = "📍 Наш адрес: Майкоп, ул. Строителей 8Б (район железного рынка)"
WORK_TIME = "🕒 Мы работаем: 10:00–19:00 каждый день, кроме понедельника"

ADDRESS_KEYWORDS = ["адрес", "где найти", "где приехать", "где вы", "где находитесь", "как найти"]
WORK_KEYWORDS = ["время работы", "работаете", "до скольки", "рабочий день", "график работы"]

THRESHOLD = 70

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    
    if any(fuzz.partial_ratio(word, text) >= THRESHOLD for word in ADDRESS_KEYWORDS):
        await update.message.reply_text(
            ADDRESS_TEXT,
            reply_to_message_id=update.message.message_id
        )
        return

    
    if any(fuzz.partial_ratio(word, text) >= THRESHOLD for word in WORK_KEYWORDS):
        await update.message.reply_text(
            WORK_TIME,
            reply_to_message_id=update.message.message_id
        )
        return


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))


app.run_polling()