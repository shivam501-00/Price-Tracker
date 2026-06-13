# 💸 Price Tracker

Automatically tracks Amazon/Flipkart product prices and sends email alerts on price drops.

## 🚀 Features
- Live price scraping from Amazon/Flipkart
- Price history stored locally in JSON
- Email alert when price drops
- Runs automatically every hour

## 🗂️ Project Structure
     price_tracker/
    ├── scraper.py       → fetches live price from product URL
    ├── storage.py       → saves/loads price history to prices.json
    ├── tracker.py       → compares current vs lowest price, triggers alert
    ├── notifier.py      → sends Gmail alert on price drop
    ├── scheduler.py     → runs tracker every hour automatically
    ├── prices.json      → local database of price history
    ├── .env             → secret credentials (never pushed to GitHub)
    └── requirements.txt → all dependencies

## ⚙️ Setup

### 1. Clone the repo
git clone https://github.com/shivam501-00/Price-Tracker.git
cd price-tracker

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Create .env file
SENDER_EMAIL=your_gmail@gmail.com
APP_PASSWORD=your_16_digit_app_password
RECEIVER_EMAIL=your_gmail@gmail.com

### 5. Run it

Track a product manually:
python tracker.py

Run automated hourly checks:
python scheduler.py

## 🛠️ Tech Used
- **requests** — fetches raw HTML from product pages
- **BeautifulSoup** — parses HTML and extracts price
- **schedule** — runs tracker automatically every hour
- **smtplib** — sends email alerts via Gmail
- **python-dotenv** — loads credentials from .env file
- **json** — stores price history locally