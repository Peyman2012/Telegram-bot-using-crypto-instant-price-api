from telegram.ext import Updater, CommandHandler
from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()
print(cg.get_price(ids='bitcoin,litecoin,ethereum,Tether', vs_currencies='usd'))


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hi Welcome to CryptoLand')


cg = CoinGeckoAPI()


def Price(bot, update):
    data_market = cg.get_coins_markets(vs_currency="usd")
    df_market = pd.DataFrame(data_market, columns=["id", "current_price"])
    df_market.set_index("id", inplace=True)
    price = df_market.loc["bitcoin"][0]
    bot.send_message(chat_id=update.message.chat_id, text=f"{price}")
    msg=update.message
    print(msg)

with open("token.txt", 'r') as f:
    Token = f.read()
updater = Updater(token=Token, base_url="https://tapi.bale.ai/bot")

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("price", Price))

updater.start_polling()
updater.idle()
