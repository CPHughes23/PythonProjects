import schedule 
import smtplib 
import requests 
from bs4 import BeautifulSoup 

city = "Hyderbad"
url = "https://google.com/search?q=" + "weather" + city
