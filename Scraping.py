# Step 1
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Step 2
headers = {'Accept-Language': 'en-US,en;q=0.8'}
url = 'https://edition.cnn.com/'
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Step 3
newstitle = soup.select('h3.cd__headline a, span.cd__headline-text')
if newstitle:
    print(newstitle[0].get_text())
else:
    print("None found ")

print("how many titles are available?", len(newstitle))

#Step 4
article_title = ['Don’t drink before your nap on the plane. It could hurt you now and later', 'Four civilians on a daring SpaceX mission complete the first commercial spacewalk', 'Viral Olympian Raygun ranked No. 1 breaker in the world by sport’s governing body', 'Israel and the Israel-Hamas war', 'Sean ‘Diddy’ Combs denied bail and will remain in federal detention, judge rules']
links = ['https://edition.cnn.com/2024/06/03/health/alcohol-planes-heart-study-wellness/index.html/' , 'https://edition.cnn.com/2024/09/12/science/spacewalk-polaris-dawn-mission-spacex/index.html', 'https://edition.cnn.com/2024/09/10/sport/raygun-ranked-number-one-breaker-spt-intl/index.html', 'https://edition.cnn.com/world/middleeast/israel', 'https://edition.cnn.com/entertainment/live-news/sean-diddy-combs-arrested-nyc-09-17-2024/index.html']

for a in soup.select('h3.cd__headline a, span.cd__headline-text'):
    title = a.get_text()
    article_title.append(title)

    href = a.attrs.get('href')
    if href.startswith('/'):
        links.append('https://edition.cnn.com' + href)
    else:
        links.append(href)

for t in soup.select('h3.cd__headline a, span.cd__headline-text'):
    article_title.append(t.get_text())
    links.append('https://edition.cnn.com' + t.attrs.get('href'))

print(article_title)
print(links)

# step 5
df = pd.DataFrame(
    {'article title': article_title,
     'link': links}
)

print(df.head())

df.to_csv('cnn_articles.csv', index=False)
