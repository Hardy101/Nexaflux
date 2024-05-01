import requests

API_KEY = 'b5e8d84233fa51c53dcb14952099ac801c533bcbe5590518bafaa3778e27763d'
PRICE_ENDPOINT = 'https://min-api.cryptocompare.com/data/price'
COINS_ENDPOINT = 'https://min-api.cryptocompare.com/data/all/coinlist'



# def get_coin_price(coin):
#   param = {
#     'fsym': coin,
#     'tsyms': 'USDT',
#     'api_key': API_KEY
# }
#   data = requests.get(PRICE_ENDPOINT, params=param)
#   data_info = data.json()
#   coin_price = data_info['USDT']
#   return coin_price

# print(get_coin_price('BITCOIN'))


# def get_coin_info(coin):
#   param = {
#     'fsym': coin,
#     'tsyms': 'USDT',
#     'api_key': API_KEY
# }
#   data = requests.get(COINS_ENDPOINT, params=param)
#   data_info = data.json()['Data'][coin]
#   name = data_info['FullName']
#   coin_name = data_info['CoinName']
#   return name, coin_name

# print(get_coin_info('ENA'))

# - Get coinlist
def get_coin_info():
  param = {
    'tsyms': 'USDT',
    'api_key': API_KEY
}
  data = requests.get(COINS_ENDPOINT, params=param)
  data_info = data.json()['Data']
  return data_info

print(get_coin_info())