#! /usr/bin/env python
# 17-decode-a-web-page
# Use the BeautifulSoup and requests Python packages to print out a
# list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://www.nytimes.com/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')
    title = soup.find_all('h2', class_="story-heading")

    print("\n".join([i.get_text() for i in title]))


if __name__ == "__main__":
    main()
