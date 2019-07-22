import telegram

bot = telegram.Bot(token = '803288229:AAF3jcyErpuDmvg2Ga9yDaZ9Djd0_9tv7vE')

#for i in bot.getUpdates():
#   print(i.message)

bot.sendMessage(chat_id=705760272, text = "Welcome!")
