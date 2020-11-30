import requests
import bs4

res = requests.get('https://www.youtube.com/feed/trending')
#print(res.text)
soup = bs4.BeautifulSoup(res.text, 'lxml')

post_titles = soup.findAll("yt-formatted-string", class_ = "style-scope ytd-video-renderer")
for i in post_titles:
    print(i)

