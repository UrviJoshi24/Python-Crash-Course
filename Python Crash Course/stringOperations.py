'''
print('Hello, world!')
print('Hello, I am urvi')
name = 'urvi'
friend = 'ishika'
print('Hello, '+friend)
print(name[0])
# in python, string is like an array of characters. We can access parts of string by using its index which starts from 0
# and array is a collection of items.
print('Lets use a for loop\n')
for character in name:
  print(character)
print('\n')
for character in friend:
  print(character)


names = 'Harry,Shubham'
print(names[0:5])
print(len(names))

fruit = 'mango'
#len =   01234
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])
print(fruit[:4])
print(fruit[:])
print(fruit[0:len(fruit)-3])
print(fruit[-3:-1]) # len-3 : len-1
'''

# string methods
# string are immutable
a = 'Urvi %&# !'
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace('r','a'))
s = 'I am amazed'
s.replace('a','x')
print(s) # here original string is not changing.
print(a.split(" "))
blogHeading = 'intRodUction to jS'
print(blogHeading.capitalize())
print(blogHeading.swapcase())
str1 = 'Welcome to Coding'
print(len(str1))
print(len(str1.center(500)))
print(str1.count("o"))
print(str1.endswith('Coding'))
b = 'Welcome to YouthfulHorribleMineral'
print(b.endswith('to',3,10))
# find() method searches for the first occurence of the given value and returns the index where it is present. for example
info = 'HIi i am urvi joshi. i am currently practing python for string operation'
print(info.find('joshi'))
# isalnum() method returns True only if the entire string only consists of A-Z,a-z,0-9.
alNum = 'WlcomeToTHEPYthonCourse'
print(alNum.isalnum())
alNum = 'WlcomeToTHEPYthonCourse0'
print(alNum.isalpha())