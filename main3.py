import telegram.ext
from pycoingecko import CoinGeckoAPI
import pandas as pd


def start(bot,update):
    bot.send_message(text="Hi Welcome to CryptoLand")
def massage_handler(update,context):
    msg = update.message.text
    print(msg)
    
cg = CoinGeckoAPI()    
def Price(bot,update):
    
    data_market = cg.get_coins_markets(vs_currency = "usd")  
    df_market = pd.DataFrame(data_market,columns=["id","current_price"])
    df_market.set_index("id",inplace=True)   
    price = df_market.loc["bitcoin"][0]
    bot.send_message(text=f"{price}")


with open("token.txt", 'r') as f:
    token = f.read()
    
updater = telegram.ext.Updater(token)


dp = updater.dispatcher
dp.add_handler(telegram.ext.CommandHandler("start", start))
dp.add_handler(telegram.ext.CommandHandler("price", Price))
dp.add_handler(telegram.ext.MassageHandler(telegram.ext.Filter.text,massage_handler))

updater.start_polling()
updater.idle()

