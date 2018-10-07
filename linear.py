import re
import requests
import time

pages = [
    "https://www.wuxiaworld.com/novel/against-the-gods",
    "https://www.wuxiaworld.com/novel/demon-hunter",
    "https://www.wuxiaworld.com/novel/martial-god-asura",
    "https://www.wuxiaworld.com/novel/monarch-of-evernight",
    ]

def get_webpage(page):
    response = requests.get(page)
    print("Getting " + str(response.url))
    return response.text


def get_chapters(pagetext):
    print("Scrape completed, begining RegEx...")
    result = []

    expr = r'<span>((\w|[\-\*\.\?\:]|\s)*)</span>'
    for match in re.finditer(expr, pagetext):
        result.append(match.group(1))

    return result


def wuxia_scrape_chapters(pagelist):
    chapters = []
    for page in pagelist:
        print("Scraping next page...")
        chapters.append(get_chapters(get_webpage(page)))

    for ch in chapters:
        print("Next Book: ")
        print(ch[:2])  # prints the first few chapters

print("Scraping...")
t = time.clock()
wuxia_scrape_chapters(pages)
print(time.clock() - t)
