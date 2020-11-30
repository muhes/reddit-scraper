import requests
import bs4

res = requests.get('https://twitter.com/mangoes45693')
soup = bs4.BeautifulSoup(res.text, 'lxml')

tweets = soup.select('.css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
print(tweets)

title = soup.select('title')
print(title)
for i in tweets:
    print(i.texts)