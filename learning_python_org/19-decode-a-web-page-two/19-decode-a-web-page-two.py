#! /usr/bin/env python
# 19-decode-a-web-page-two
#
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of
# the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print out the text
# to the screen so that you can read the full article without having to click any buttons.

import requests
from bs4 import BeautifulSoup


def main():
    for i in range(1, 5, 1):
        r = requests.get("https://stackoverflow.com/questions/tagged/python?page=" + str(i))
        data = r.text
        soup = BeautifulSoup(data, "html.parser")

        for question in soup.select(".question-summary"):
            for h3 in question.select("h3"):
                print("# " + h3.text + " #")
            for excerpt in question.select(".excerpt"):
                print(excerpt.text.lstrip())


if __name__ == '__main__':
    main()
