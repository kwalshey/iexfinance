from iexfinance.stocks import Stock
import os

api_token = "Tsk_600228e72e1643768e1a528fa90cb1e9"
api_version = "iexcloud-sandbox"

os.environ["IEX_TOKEN"] = api_token
os.environ["IEX_API_VERSION"] = api_version
os.environ["IEX_OUTPUT_FORMAT"] = "pandas"


stock = Stock("AAPL")
hi = stock.get_advanced_stats()

print("done")