import logging as log

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

if __name__ == '__main__':
    log.basicConfig(level=log.INFO)

    cg = CoinGeckoAPI()
    bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
    log.info(f"type of bitcoin_data is {type(bitcoin_data)}")
    # log.info(f"bitcoin_data is \n{bitcoin_data}")
    log.info(f"head of bitcoin_data is \n{pd.DataFrame(bitcoin_data)[0:5].to_string()}")
    log.info(f"columns of bitcoin_data are \n{pd.DataFrame(bitcoin_data).columns}")
    bitcoin_price_data = bitcoin_data['prices']
    log.info(f"bitcoin_price_data[0:5] is \n{bitcoin_price_data[0:5]}")
    pricesDF = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
    log.info(f"pricesDF is \n{pricesDF}")
    pricesDF['datetime'] = pricesDF['TimeStamp'].apply(lambda d: datetime.datetime.fromtimestamp(d/1000.0))
    log.info(f"pricesDF is \n{pricesDF}")
    candlestick_data = pricesDF.groupby(pricesDF.datetime, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
    log.info(f"candlestick_data is \n{candlestick_data[0:5].to_string()}")\

    fig = go.Figure(data=[go.Candlestick(x=candlestick_data['datetime'],
                                         open=candlestick_data['Price']['first'],
                                         high=candlestick_data['Price']['max'],
                                         low=candlestick_data['Price']['min'],
                                         close=candlestick_data['Price']['last'])
                          ])
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.show()