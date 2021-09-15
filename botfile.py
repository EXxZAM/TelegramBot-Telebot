import telebot

bot = telebot.TeleBot("token") #! TOKEN WITHOUT THE bot AT THE START 
#? Example: bot24352442342:AAFSDVFVVDFGFGDSF => 224352442342:AAFSDVFVVDFGFGDSF

@bot.message_handler(func= lambda command: (command.text).lower() == '/start' )
def start(message):
    bot.reply_to(message,"Replying!" )



bot.polling()
