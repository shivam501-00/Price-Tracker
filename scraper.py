import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_price(url):
    response= requests.get(url,headers=HEADERS) #headers are used to mimic a real browser visit, which can help avoid being blocked by the website. The User-Agent string identifies the type of browser and operating system making the request.
    
    soup = BeautifulSoup(response.text,'html.parser') #html.parser is a built-in parser in Python that can parse HTML documents. BeautifulSoup creates a parse tree from the HTML, which allows us to navigate and search for specific elements easily.

  # Amazon price classes
    possible_classes = [
        "a-price-whole",
        "a-offscreen",
        "priceToPay",
    ]

    for class_name in possible_classes:
        price_tag = soup.find(class_=class_name)
        if price_tag:
            print(f"✅ Found price using class: {class_name}")
            # print(f"Raw price text: '{price_tag.text.strip()}'")
            price_text = price_tag.text.strip().replace("₹", "").replace(",", "").replace(".", "")
            # remove anything that's not a digit
            price_text = ''.join(filter(str.isdigit, price_text))
            return float(price_text)

    # Nothing worked — dump HTML for inspection
    print("❌ Not found. Saving debug.html...")
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    return None

if "__main__" == __name__:
    url= input("Enter the URL of the product: ")
    price =get_price(url)
    print(f"The current price of the product is: ₹{price}")