import smtplib 
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()  # Load environment variables from .env file
SENDER_EMAIL   = os.getenv("SENDER_EMAIL")
APP_PASSWORD   = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def send_alert(url,current_price,lowest_price):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f"Price Alert: Price Drop Detected! Now at ₹{current_price}"

    body= f"""
    🔥 Price Drop Alert! 🔥
    Hey Shivam,
    price of the product you are tracking has dropped!
    Product URL: {url}
    New Price: ₹{current_price}
    you save : ₹{lowest_price - current_price} from the lowest price seen before.
    
    Go grab it! 🚀

    """

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('SMTP.gmail.com',587) as server:
        server.ehlo()             # identify ourselves to the server
        server.starttls()         # encrypt the connection
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

    print(f"📧 Alert email sent to {RECEIVER_EMAIL}!")
