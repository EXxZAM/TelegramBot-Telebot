

# Telegram Bot with Telebot
📝
Control a telegram bot easily with this package!

## Needed Packages 

🐍
```bash
pip install telebot
pip install pyTelegramBotAPI
```

## Telebot Example

🐍
```bash
import telebot
bot = telebot.TeleBot("token") #! TOKEN WITHOUT THE bot AT THE START 
#? Example: bot24352442342:AAFSDVFVVDFGFGDSF => 224352442342:AAFSDVFVVDFGFGDSF

#! Handling Sent Messages
@bot.message_handler(func= lambda command: (command.text).lower() == 'command' )
def getCommand(message):
    bot.reply_to(message,"Replying!" )
#! command example => /start , /help etc.
bot.polling()

```


## Made By ❤
👨‍💻 This python project is made by Mahdi Olamaei aka exxzam


🔗 [instagram.com/mahdi12ad](https://instagram.com/mahdi12ad)


🔗 [t.me/exxzam](https://t.me/exxzam)


🔗 [Aparat.com](https://www.aparat.com/iranfun200)




