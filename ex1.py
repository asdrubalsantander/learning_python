#Ex1
import datetime

now = datetime.datetime.now()
name = input("Hello, how it's your name?")
age = int(input(name +", and your age is?"))
print('The year will be: '+str(((100-age)+now.year))+ ' in your 100 year!')
