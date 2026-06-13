# tracker.py

from scraper import get_price
from notifyer import send_alert
from storage import save_price, get_lowest_price

def track(url):
    print(f"\n🔍 Checking price...")
    
    # Step 1: Scrape current price
    current_price = get_price(url)
    
    if current_price is None:
        print("❌ Could not fetch price. Check the URL or try again.")
        return
    
    print(f"💰 Current price: ₹{current_price}")
    
    # Step 2: Get lowest price we've seen before
    lowest_price = get_lowest_price(url)
    
    # Step 3: Save current price to history
    save_price(url, current_price)
    
    # Step 4: Compare and alert
    if lowest_price is None:
        print("📦 First time tracking this product. Price saved!")
    elif current_price < lowest_price:
        print(f"🔥 PRICE DROP! Lowest ever was ₹{lowest_price} → now ₹{current_price}")
        send_alert(url, current_price, lowest_price)
    elif current_price == lowest_price:
        print(f"✅ Price is at its lowest: ₹{current_price}")
    else:
        print(f"📈 Price is higher than lowest. Lowest seen: ₹{lowest_price}")

def main():
    print("=== 💸 Price Tracker ===")
    url = input("\nPaste product URL: ").strip()
    track(url)

if __name__ == "__main__":
    main()