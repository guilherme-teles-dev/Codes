import feedparser
import selenium as sl
url = 'https://news.google.com/foryou?hl=en-US&gl=US&ceid=US%3Aen'
print(dir(feedparser))
f = feedparser.parse(url)
print(f)
print()
print(f.keys())
print()
print(f.headers)
print()
print(f.feed.keys())
print()
print(len(f.entries))
print()
print(f.href)
