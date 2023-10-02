from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from pycoingecko import CoinGeckoAPI
import pandas as pd





cg = CoinGeckoAPI()


def market_price():
    data_market = cg.get_coins_markets(vs_currency="usd")
    df_market = pd.DataFrame(data_market, columns=["id", "current_price"])
    df_market.set_index("id", inplace=True)
    return df_market


def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi Welcome to CryptoLand')


def massage_handler(bot,update):
    msg = update.message.text
    df_market = market_price()
    try:

        Price = df_market.loc[msg][0]
        bot.send_message(chat_id=update.message.chat_id, text=f"{msg}: {Price}$")
    except:
        bot.send_message(chat_id=update.message.chat_id, text="Try again!!!!")


def list_coin(bot,update):
    df_market = market_price()
    bot.send_message(chat_id=update.message.chat_id, text=list(df_market.index))

Token = '1226131623:uQiJSmRG7mwRsvj7Fc8iUWyuOkOy7eQ4qHC73KKl'
updater = Updater(token=Token, base_url="https://tapi.bale.ai/bot")

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("list", list_coin))
dp.add_handler(MessageHandler(Filters.text, massage_handler))

updater.start_polling()
updater.idle()