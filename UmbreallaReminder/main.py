import schedule 
import smtplib 
import requests 
from bs4 import BeautifulSoup 

city = "Tempe"
url = "https://google.com/search?q=weatherTempe"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

response = requests.get(url, headers).text


# print(html)

soup = BeautifulSoup(response,'html.parser') 

# print(soup.prettify())

temperature = soup.find('span', attrs={'class': 'BNeawe iBp4i AP7Wnd'})
time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'})

print(temperature)
print(time_sky)


# formatting data 
# sky = time_sky.split('\n')[1] 

# print(sky)