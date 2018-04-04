#! /usr/bin/env python
# 19-decode-a-web-page-two
#
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of
# the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print out the text
# to the screen so that you can read the full article without having to click any buttons.

import requests
from bs4 import BeautifulSoup
import re


def main():
    r = requests.get("https://stackoverflow.com/questions/tagged/python")
    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    for node in soup.findAll("div", {"class": "summary"}):
        #print(re.match(r'([a-zA-Z])', ''.join(node.findAll(text=True))))
        print(''.join(node.findAll(text=True)))



if __name__ == '__main__':
    main()
