import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.com/Kmise-Beginners-Students-Hygrometer-Shoulder/dp/B094JCQ1KT/ref=sr_1_13_sspa?" \
      "keywords=violin&qid=1700095252&sr=8-13-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&smid=A3I0DUQB6I74AP&th=1"

header = {
"Accept-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
              " Chrome/119.0.0.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
          " application/signed-exchange;v=b3;q=0.7"
}
response = requests.get(url, headers=header)
webpage = response.content
soup = BeautifulSoup(webpage, 'lxml')

print(soup)
