import telebot 
from config import token
import datetime
from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['feed'])
def feed(self, feed_interval = 20, hp_increase = 10 ):
    current_time = datetime.now()  
    delta_time = timedelta(hours=feed_interval)  
    if (current_time - self.last_feed_time) > delta_time:
        self.hp += hp_increase
        self.last_feed_time = current_time
        return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
    else:
        return f"Следующее время кормления покемона: {current_time-delta_time}"  


bot.infinity_polling(none_stop=True)

