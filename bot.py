from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import re
from rapidfuzz import fuzz
import string

TOKEN ="8632066324:AAHTAri1Owiv_T7-OfebMF9vFsBhQxDOFmU"

# Тексты ответов
ADDRESS_TEXT = "📍 Наш адрес: Майкоп, ул. Строителей 8Б (район железного рынка)"
WORK_TIME = "🕒 Мы работаем: 10:00–19:00 каждый день, кроме понедельника"
BLACKLIST = ["сколько", "есть"]  

# Ключевые слова
ADDRESS_KEYWORDS = ["адрес", "где найти", "где приехать", "где вы", "где находитесь", "как найти"]
WORK_KEYWORDS = ["время работы", "работаете", "до скольки", "рабочий день", "график работы"]

# Порог похожести для fuzzy поиска (0-100)
THRESHOLD = 85

# Функция проверки релевантности текста
def is_relevant(text: str, keywords: list) -> bool:
    text = text.lower().translate(str.maketrans('', '', string.punctuation)).strip()

    if text in BLACKLIST:
        return  False

    if "сколько" in text and "работ" not in text:
        return False

    for word in keywords:
        clean_word = word.lower().translate(str.maketrans('', '', string.punctuation))

        if re.search(r'\b' + re.escape(clean_word) + r'\b', text):
            return True

        if fuzz.partial_ratio(clean_word, text) >= THRESHOLD:
            return True

    return False

# Обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if is_relevant(text, ADDRESS_KEYWORDS):
        await update.message.reply_text(
            ADDRESS_TEXT,
            reply_to_message_id=update.message.message_id
        )
        return

    if is_relevant(text, WORK_KEYWORDS):
        await update.message.reply_text(
            WORK_TIME,
            reply_to_message_id=update.message.message_id
        )
        return

# Создание приложения и добавление обработчика
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Запуск бота
app.run_polling()