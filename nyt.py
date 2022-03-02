from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
}
url = 'https://www.nytimes.com/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')

for item in soup.select('div.story-wrapper'):
    try:
        print('----------------------------------------')
        headline = item.find('h3').get_text()
        print(headline)
    except Exception as e:
        raise e
