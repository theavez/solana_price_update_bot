import requests

headers = {
"Accept-Language" : "en-US,en;q=0.5",
"User-Agent": "Defined",
}

url = 'https://data-api.cryptocompare.com/spot/v1/latest/tick'
params = {
    'instruments':'SOL-USDT',
    'apply-mapping': True,
    'market':'binance',
    'api_key':'YOUR CRYPTOCOMPARE API KEY'
}
# For getting different crypto coin. You can update the instruments param e.g ('instruments':'['BTC-USDT','ETH-USDT'],)

def get_price():

    response = requests.get(url=url,params=params,headers=headers)
    response.raise_for_status()
    data = (response.json())['Data']['SOL-USDT']

    current_hour = {'open':data['CURRENT_HOUR_OPEN'],
                    'high':data['CURRENT_HOUR_HIGH'],
                    'low':data['CURRENT_HOUR_LOW'],
                    'total trade':data['CURRENT_HOUR_TOTAL_TRADES'],
                    'buy trades': data['CURRENT_HOUR_TOTAL_TRADES_BUY'],
                    'sell trades': data['CURRENT_HOUR_TOTAL_TRADES_SELL']
                }

    current_day = {
                    'open':data['CURRENT_DAY_OPEN'],
                    'high':data['CURRENT_DAY_HIGH'],
                    'low':data['CURRENT_DAY_LOW'],
                    'total trade':data['CURRENT_DAY_TOTAL_TRADES'],
                    'buy trades': data['CURRENT_DAY_TOTAL_TRADES_BUY'],
                    'sell trades': data['CURRENT_DAY_TOTAL_TRADES_SELL']
            }

    moving_24_hour = {
                    'open':data['MOVING_24_HOUR_OPEN'],
                    'high':data['MOVING_24_HOUR_HIGH'],
                    'low':data['MOVING_24_HOUR_LOW'],
                    'total trade':data['MOVING_24_HOUR_TOTAL_TRADES'],
                    'buy trades': data['MOVING_24_HOUR_TOTAL_TRADES_BUY'],
                    'sell trades': data['MOVING_24_HOUR_TOTAL_TRADES_SELL']
    }

    current_week = {
                    'open':data['CURRENT_WEEK_OPEN'],
                    'high':data['CURRENT_WEEK_HIGH'],
                    'low':data['CURRENT_WEEK_LOW'],
                    'total trade':data['CURRENT_WEEK_TOTAL_TRADES'],
                    'buy trades': data['CURRENT_WEEK_TOTAL_TRADES_BUY'],
                    'sell trades': data['CURRENT_WEEK_TOTAL_TRADES_SELL']
    }

    moving_7_day = {
                    'open':data['MOVING_7_DAY_OPEN'],
                    'high':data['MOVING_7_DAY_HIGH'],
                    'low':data['MOVING_7_DAY_LOW'],
                    'total trade':data['MOVING_7_DAY_TOTAL_TRADES'],
                    'buy trades': data['MOVING_7_DAY_TOTAL_TRADES_BUY'],
                    'sell trades': data['MOVING_7_DAY_TOTAL_TRADES_SELL']
    }

    current_month = {
                    'open':data['CURRENT_MONTH_OPEN'],
                    'high':data['CURRENT_MONTH_HIGH'],
                    'low':data['CURRENT_MONTH_LOW'],
                    'total trade':data['CURRENT_MONTH_TOTAL_TRADES'],
                    'buy trades': data['CURRENT_MONTH_TOTAL_TRADES_BUY'],
                    'sell trades': data['CURRENT_MONTH_TOTAL_TRADES_SELL']
    }

    moving_30_days = {
                    'open':data['MOVING_30_DAY_OPEN'],
                    'high':data['MOVING_30_DAY_HIGH'],
                    'low':data['MOVING_30_DAY_LOW'],
                    'total trade':data['MOVING_30_DAY_TOTAL_TRADES'],
                    'buy trades': data['MOVING_30_DAY_TOTAL_TRADES_BUY'],
                    'sell trades': data['MOVING_30_DAY_TOTAL_TRADES_SELL']
    }

    moving_90_days = {
                    'open':data['MOVING_90_DAY_OPEN'],
                    'high':data['MOVING_90_DAY_HIGH'],
                    'low':data['MOVING_90_DAY_LOW'],
                    'total trade':data['MOVING_90_DAY_TOTAL_TRADES'],
                    'buy trades': data['MOVING_90_DAY_TOTAL_TRADES_BUY'],
                    'sell trades': data['MOVING_90_DAY_TOTAL_TRADES_SELL']
    }

    update = f"SOLANA PRICE : {data['PRICE']} $\n\nCURRENT HOUR:\nopen - {current_hour['open']} $\nhigh - {current_hour['high']} $\nlow - {current_hour['low']} $\ntotal trade - {current_hour['total trade']} trades\nbuy trades - {current_hour['buy trades']} trades\nsell trades - {current_hour['sell trades']} trades\n\n"
    update += f"CURRENT DAY:\nopen - {current_day['open']} $\nhigh - {current_day['high']} $\nlow - {current_day['low']} $\ntotal trade - {current_day['total trade']} trades\nbuy trades - {current_day['buy trades']} trades\nsell trades - {current_day['sell trades']} trades\n\n"
    update += f"CURRENT WEEK:\nopen - {current_week['open']} $\nhigh - {current_week['high']} $\nlow - {current_week['low']} $\ntotal trade - {current_week['total trade']} trades\nbuy trades - {current_week['buy trades']} trades\nsell trades - {current_week['sell trades']} trades\n\n"
    update += f"CURRENT MONTH:\nopen - {current_month['open']} $\nhigh - {current_month['high']} $\nlow - {current_month['low']} $\ntotal trade - {current_month['total trade']} trades\nbuy trades - {current_month['buy trades']} trades\nsell trades - {current_month['sell trades']} trades\n\n"
    update += f"MOVING 90 DAYS:\nopen - {moving_90_days['open']} $\nhigh - {moving_90_days['high']} $\nlow - {moving_90_days['low']} $\ntotal trade - {moving_90_days['total trade']} trades\nbuy trades - {moving_90_days['buy trades']} trades\nsell trades - {moving_90_days['sell trades']} trades\n"
    return update