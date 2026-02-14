yob= int(input('enter year of birth '))
year= int(input('enter current year '))
age=year-yob
print('your age is',age)
if age >=18:
    print('you are eligible for vote')
    print('make sure to choose a good leader')
else:
    print('not eligible to vote')
    print('thank u for visiting us')