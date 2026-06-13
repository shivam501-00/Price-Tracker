import schedule
import time
from tracker import track
from storage import load_data

def check_all():
    print("\n⏰ Running scheduled price check...")
    data = load_data()
    urls = list(data.keys())
    
    if not urls: 
        print("📭 No products being tracked yet. Add some URLs first!")
        return
    
    for url in urls:
        track(url)
        print("\n✅ Done. Waiting for next check...")

schedule.every(1).hours.do(check_all)

check_all()  # Run immediately on start


print("⏳ Scheduler is running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute for pending tasks
    

