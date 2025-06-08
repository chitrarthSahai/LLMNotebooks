#We are creating some utils function to break the code in a btter way.
import requests
from pymongo.collection import Collection
import datetime, random

api_key = "CG-YgaSDYyvsiDQsZvTB8KNjJcR"

headers = {
    "x-cg-demo-api-key": api_key
}

def get_random_datetime():
    return datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 7))

def get_coin_price(coin_ids, currency):
    crypto_ids = ','.join(coin_ids)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_ids}&vs_currencies={currency}"
    data = requests.get(url, headers=headers).json()
    return dict([(coin_id, data[coin_id][currency]) for coin_id in data])


def seed_data(collection: Collection):
    collection.insert_many([
        {
            "name": "Bulls",
            "metadata": {
                "description": "Coins to buy",
                "currency": "usd",
                "date_created": get_random_datetime()
            },
            "coins":[
                {"coin": "bitcoin", "note": "The most popular coin", "date_added": get_random_datetime()},
                {"coin": "ethereum", "note": "The second most popular coin", "date_added": get_random_datetime()}
            ]
        },
        {
            "name": "Bears",
            "metadata": {
                "description": "Coins to hold or sell",
                "currency": "usd",
                "date_created": get_random_datetime()
            },
            "coins":[
                {"coin": "bitcoin", "note": "The most popular coin", "date_added": get_random_datetime()},
                {"coin": "ethereum", "note": "The second most popular coin", "date_added": get_random_datetime()}
            ]
        }
    ])