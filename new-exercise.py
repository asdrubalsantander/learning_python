#! /usr/bin/env python
# new-exercise.py
# A simple script that creates the folder, the python file and the readme for the given exercise.

import os
import requests
from bs4 import BeautifulSoup
import textwrap


def get_exercise_metadata(base_url, exercise_number):
    r = requests.get(base_url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    left = soup.find('div', {'class': 'left'})
    ul = left.find('ul')
    all_li = ul.find_all('li')
    a = all_li[exercise_number - 1].find('a')
    name_exercise = format_name(exercise_number, a.text)
    url_exercise = a['href']

    return name_exercise, url_exercise, a.text


def format_name(exercise_number, name_unformatted):
    return (str(exercise_number) + name_unformatted.replace(" ", "-")).lower()


def get_exercise_data(url, exercise_number):
    id = "exercise-" + str(exercise_number) + "-and-solution"

    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    exercise_text = soup.find('h2', {'id':id}).find_next('p').text

    exercise_text_wrapped = textwrap.wrap(exercise_text, 100)

    return exercise_text_wrapped


if __name__ == '__main__':

    number = int(input("What number of exercise are you going to do? \n Number: "))

    base_url = "https://www.practicepython.org/"

    path, url, name_unformatted = get_exercise_metadata(base_url, number)

    # Create the directory to hold the exercise
    if not os.path.exists(path):
        os.makedirs(path)

        # cd into the directory
        os.chdir(path)

        exercise_text = get_exercise_data(base_url + url, number)

        # Create 2 files exercise_name.py and README.md
        with open(path + ".py", 'w') as python_exercise, open("README.md", 'w') as readme:
            python_exercise.write("#! /usr/bin/env python\n")
            python_exercise.write("# " + path + "\n")
            python_exercise.write("# \n")
            for text in exercise_text:
                python_exercise.write("# " + text + "\n")

            readme.write("# " + str(number) + " - " + name_unformatted + "\n")
            readme.write("### Main:\n")
            readme.write("!['Result'](" + path + ".png)")

        # chmod +x
        os.chmod(path + ".py", 0o775)

    else:
        print("The directory for that exercise already exist.")