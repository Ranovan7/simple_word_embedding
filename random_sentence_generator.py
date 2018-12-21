import requests
import json
import time
import pprint

# getting random quotes using API from talaikis.com, you rock man!
url = "https://talaikis.com/api/quotes"
save_file = "random_quotes2.json"
quotes = []

# repeat the request until we get desireable amount of data
while True:
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
        quotes.extend(data)
        print(data[3])
        print(f"Data Count : {len(quotes)}")
    else:
        print("Failed to get Data, code :", req.status_code)
    if len(quotes) >= 1000:
        break
    else:
        time.sleep(1)

# dump data to json
json.dump(quotes, open(save_file, 'w'), indent=4)
