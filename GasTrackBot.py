import telebot
from telebot import types
import json

bot = telebot.TeleBot("TOKEN", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, Welcome to the GasTracker!\n\nClick /options for more options..")

@bot.message_handler(commands=['options'])
def send_welcome(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Last Block')
    itembtn2 = types.KeyboardButton('Gas Price')
    itembtn3 = types.KeyboardButton('ETH Price')
    itembtn4 = types.KeyboardButton('Suggest Base Fee')
    itembtn5 = types.KeyboardButton('Gas Used Ratio')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5)
    bot.send_message(chat_id, "Choose Your Option:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    f = open('JSON/data.json')
    data = json.load(f)
    f.close()

    if(message.text=='Last Block'):
        bot.reply_to(message, 'Date Time: '+str(data['timestamp'])
                             +'\nLast Block: '+str(data['LastBlock']))
    elif(message.text == 'Gas Price'):
        bot.reply_to(message, 'Date Time: '+str(data['timestamp'])
                             +'\nSafeGasPrice: ' + str(data['SafeGasPrice']) +' gwei'
                             +'\nProposeGasPrice: '+ str(data['ProposeGasPrice']) +' gwei'
                             +'\nFastGasPrice: '+ str(data['FastGasPrice']) +' gwei'
                             +'\n\nSafeGasPrice($): ' + str(round(float(data['SafeGasPrice'])*float(data['ethusd']), 2)) + ' $'
                             +'\nProposeGasPrice($): ' + str(round(float(data['ProposeGasPrice'])*float(data['ethusd']), 2)) + ' $'
                             +'\nFastGasPrice($): ' + str(round(float(data['FastGasPrice'])*float(data['ethusd']), 2)) + ' $')
    elif (message.text == 'ETH Price'):
        bot.reply_to(message, 'Date Time: '+str(data['timestamp'])
                             +'\nETH/BTC: ' + str(data['ethbtc'])
                             +'\nETH/USD: ' + str(data['ethusd']))
    elif (message.text == 'Suggest Base Fee'):
        bot.reply_to(message, 'Date Time: '+str(data['timestamp'])
                             +'\nsuggestBaseFee: ' + str(data['suggestBaseFee']))
    elif (message.text == 'Gas Used Ratio'):
        bot.reply_to(message, 'Date Time: '+str(data['timestamp'])
                             +'\ngasUsedRatio: ' + str(data['gasUsedRatio']))
    else:
        bot.reply_to(message, 'Click /options for more options..')

bot.polling()