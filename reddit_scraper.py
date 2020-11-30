import requests
import bs4

res = requests.get('https://www.reddit.com/')

soup = bs4.BeautifulSoup(res.text, 'lxml')

post_title_class = '._eYtD2XCVieq6emjKBH3m'
post_titles = soup.findAll("h3")
#, class_ = "_eYtD2XCVieq6emjKBH3m"
#post_titles = soup.select(post_title_class)
for j in soup.findAll("h3"):
    print(j)


def topTitles(post_titles):
    for title in post_titles:
        print(title)

def countWord(word):
    count = 0
    for title in post_titles:
        if word in title.text:
            count += 1
    print(count)

print("Welcome to reddit scraper\n")
print("Press 1 to get top titles\n")
print("Enter word to get word count\n")
value = ""
while (value != "exit"):
    value = input("Select a command:\n")
    if (value == "1"):
        topTitles(post_titles)
    else:
        countWord(value)


