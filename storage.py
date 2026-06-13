import os
import json
from datetime import datetime

STORAGE_FILE = 'prices.json'

def load_data():
    if not os.path.exists(STORAGE_FILE):
        return {}
    with open(STORAGE_FILE, 'r') as f:
        return json.load(f) #loads json data in dictionary format to read

    
def save_price(url, price):
    data = load_data()
     

    if url not in data:
        data[url] = []

    data[url].append({
        "price": price,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_lowest_price(url):
    data = load_data()
    
    if url not in data or len(data[url]) == 0:
        return None
    
    # Extract all prices and return the minimum
    all_prices = [entry["price"] for entry in data[url]]
    return min(all_prices)