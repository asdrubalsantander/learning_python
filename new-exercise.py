#! /usr/bin/env python
# new-exercise.py
# A simple script that creates the folder, the python file and the readme for the given exercise.

import os

if __name__ == '__main__':

    path = input("What is the name of the new exercise: ")

    # Create the directory to hold the exercise
    if not os.path.exists(path):
        os.makedirs(path)

    # cd into the directory
    os.chdir(path)

    # chmod +x
    os.chmod(path + ".py", 0o775)

    # Create 2 files exercise_name.py and README.md
    with open(path + ".py", 'w') as python_exercise, open("README.md", 'w') as readme:
        python_exercise.write("#! /usr/bin/env python\n")
        python_exercise.write("# " + path)

        readme.write("!['Result'](" + path + ".png)")
