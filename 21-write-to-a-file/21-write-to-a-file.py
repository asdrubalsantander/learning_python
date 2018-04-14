#! /usr/bin/env python
# 21-write-to-a-file
# 
# Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play
# with some different code, use the code from the solution), and instead of printing the results to a
# screen, write the results to a txt file. In your code, just make up a name for the file you are
# saving to.

from bs4 import BeautifulSoup
import requests
import textwrap


def main():
    url = 'https://www.reddit.com/'
    r = requests.get(url)
    r_html = r.text

    soup = BeautifulSoup(r_html, 'html.parser')

    with open("21-write-to-a-file.txt", "w") as file:
        for title in soup.select(".title.may-blank.outbound"):
            file.write("# " + textwrap.fill(title.text,100) + " #\n")


if __name__ == '__main__':
    main()