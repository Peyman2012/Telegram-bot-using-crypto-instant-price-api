import telegram.ext
from pycoingecko import CoinGeckoAPI
import pandas as pd

with open("token.txt", 'r') as f:
    token = f.read()
    
updater = telegram.ext.Updater(token)
  
cg = CoinGeckoAPI()    
def market_price():#def market_price(msg)
    
    data_market = cg.get_coins_markets(vs_currency = "usd")  
    df_market = pd.DataFrame(data_market,columns=["id","current_price"])
    df_market.set_index("id",inplace=True)
    # Price = df_market.loc[msg][0]  
    return df_market
    #return Price


def start(update,context):
    update.message.reply_text("Hi Welcome to CryptoLand")

def massage_handler(update,context):
    msg = update.message.text
    df_market = market_price()
    Price = df_market.loc[msg][0]
    #Price = market_price(msg)
    update.message.reply_text(f"{msg}: {Price}$")



dp = updater.dispatcher
dp.add_handler(telegram.ext.CommandHandler("start", start))
dp.add_handler(telegram.ext.CommandHandler("price", market_price))
dp.add_handler(telegram.ext.MassageHandler(telegram.ext.Filter.text,massage_handler))

updater.start_polling()
updater.idle()

