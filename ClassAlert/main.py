import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


TELEGRAM_BOT_TOKEN = "7799261711:AAFywlzB3DneZV-9ZGseKYEP_CtlOfmGEhw"
TELEGRAM_CHAT_ID = "822249831"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "disable_notification":False}
    requests.post(url, json=payload)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
service = Service(r"/Users/caseyhughes/Downloads/chromedriver-mac-arm64/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://catalog.apps.asu.edu/catalog/classes/classlist?campusOrOnlineSelection=C&catalogNbr=412&honors=F&promod=F&searchType=all&subject=CSE&term=2257")


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "class-results-cell.seats"))
    )
except:
    print("Element not found, maybe it's still loading.")

while True:
    driver.refresh()
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    size = soup.find_all('div', class_='class-results-cell seats')

    for div in size:
        text_div = div.find("div", class_="text-nowrap")
        if text_div:
            seat_text = text_div.get_text(strip=True)
            print(seat_text)
            if "0 of 175" not in seat_text:
                send_telegram_message("Class has Open seats")

    print("Refreshed at:", time.strftime("%H:%M:%S"))

    time.sleep(30)