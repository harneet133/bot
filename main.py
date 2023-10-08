import telebot
import pyjokes

# Replace 'YOUR_BOT_TOKEN' with your actual bot token obtained from BotFather
TOKEN = '6522032039:AAHrpyL0uJ6vOIGQRHlKi_g7dg0ty8QogRI'

# Create an instance of the bot
bot = telebot.TeleBot(TOKEN)

# Handle the '/start' command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Hi there! I'm your joke bot. Send /joke to get a random joke.")

# Handle the '/joke' command
@bot.message_handler(commands=['joke'])
def handle_joke(message):
    joke_text = pyjokes.get_joke()
    bot.send_message(message.chat.id, joke_text)

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "I don't understand. Send /joke to get a random joke.")

# Start the bot
bot.polling()
