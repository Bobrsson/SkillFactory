import telebot

TOKEN = '1801686196:AAEdo835mu298uTzr91WacsE9YpgUhUqB-E'

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткойн': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD',
}
@bot.message_handler(content_types=['voice',])
def function_name(message):
    bot.send_message(message.chat.id, "У тебя красивый голос.")

# Обрабатываются все сообщения содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message('Чтобы начать работу с данным ботом, введите команду в следующем формате: <имя валюты> <в какую валюту перевести> <кол-во переводимой валюты>')

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

# Обрабатывается все мемесы.
@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
    bot.reply_to(message,  f"Nice meme XDD.,  {message.chat.username}")

bot.polling(none_stop=True)