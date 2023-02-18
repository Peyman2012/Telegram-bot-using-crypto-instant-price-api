import telegram.ext
from pycoingecko import CoinGeckoAPI
import pandas as pd
with open("token.txt", 'r') as f:
    token = f.read()
    
updater = telegram.ext.Updater(token)

def start(update,context):
    update.message.reply_text("Hi Welcome to CryptoLand")
def massage_handler(update,context):
    msg = update.message.text
    print(msg)
    
cg = CoinGeckoAPI()    
def Price(update,context):
    
    data_market = cg.get_coins_markets(vs_currency = "usd")  
    df_market = pd.DataFrame(data_market,columns=["id","current_price"])
    df_market.set_index("id",inplace=True)   
    price = df_market.loc["bitcoin"][0]
    update.message.reply_text(f"{price}")



dp = updater.dispatcher
dp.add_handler(telegram.ext.CommandHandler("start", start))
dp.add_handler(telegram.ext.CommandHandler("price", Price))
dp.add_handler(telegram.ext.MassageHandler(telegram.ext.Filter.text,massage_handler))

updater.start_polling()
updater.idle()

