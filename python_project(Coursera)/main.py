# import json
#
# with open("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
#           "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json") as json_file:
#     apple_json = json.load(json_file)
#
# print(apple_json)
# Yahoo finance
import yfinance as yf
# Download historical data for a stock
msft = yf.Ticker("MSFT")
msft_data = msft.history(period="max")

# Display the downloaded data
print(msft_data.head())
