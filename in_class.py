# Code Wars checkin
# Mostly good

# REGEX IN PYTHON

# Regular Expressions ('regex') is a standardized grammar for reading and formatting strings. 
# It is ubiquitous (used by many programming languages) and is an essential tool for applications
# that read lots of text (e.g., web scrapers)

# Regex has its own grammar that any programming language, given the right modules, can utilize.

from argparse import Namespace
import re
from tkinter.font import names
print(re)

# compile

# list of regex methods in Python worth knowing:
# re.compile()
# re.match()
# re.findall()
#re.search()


string_dict = {}

string_dict['christopher_string'] = 'John Wick is honestly the coolest movie character ever. No matter how much pressure he is put under, he is always able to perform -- I doubt that anyone can get the drop on him! Is there any actor more interesting than Keanu Reeves, as well?'
string_dict['mark_string'] = "Kevin Hart was born on July 6, 1979 in Philadelphia, Pennsylvania. He is known for being a comedian doing stand-up comedy and for being an actor. He was raised by his mother, Nancy, and is the youngest of two boys. His father, Henry Hart, battled with cocaine addiction and was in and out of jail, so he was rarely around during Kevin Hart's childhood. However, since Kevin's childhood, his father has cleaned himself up and the two of them have reconnected. Kevin Hart took to comedy as a way to relieve himself from all of his pain that he endured during his childhood. He used humor as a coping mechanism to make everyone laugh about the situations that he has been through. "
string_dict['bryan_string'] = "Kangaroos are just T-Rexes with Deer heads that are probably good for basketball despite their short arms"
string_dict['george_string'] = 'Pineapple does belong on pizza. For those who say it doesn\'t, consider this: your taste buds are dead. The sweetness of the pineapple combined with the savory and salty, is unmatched.  Banana however; does not.'
string_dict['cyrus_string'] = 'A hamburger, or simply burger, is a food consisting of fillings—usually a patty of ground meat, typically beef—placed inside a sliced bun or bread roll. Hamburgers are often served with cheese, lettuce, tomato, onion, pickles, bacon, or chilis; condiments such as ketchup, mustard, mayonnaise, relish, or a "special sauce", often a variation of Thousand Island dressing; and are frequently placed on sesame seed buns. A hamburger topped with cheese is called a cheeseburger.'
string_dict['jessica_string'] = 'james bond, also known as 007. eries focuses on a fictional British Secret Service agent created in 1953 by writer Ian Fleming, who featured him in twelve novels and two short-story collections. Since Flemings death in 1964, eight other authors have written authorised Bond novels or novelisations: Kingsley Amis, Christopher Wood, John Gardner, Raymond Benson, Sebastian Faulks, Jeffery Deaver, William Boyd, and Anthony Horowitz. The latest novel is With a Mind to Kill by Anthony Horowitz, published in May 2022'
string_dict['juneun_string'] = 'Robert John Downey Jr. (born April 4, 1965) is an American actor and producer. His career has been characterized by critical and popular success in his youth, followed by a period of substance abuse and legal troubles, before a resurgence of commercial success later in his career. In 2008, Downey was named by Time magazine among the 100 most influential people in the world, and from 2013 to 2015, he was listed by Forbes as Hollywood\'s highest-paid actor.'
string_dict['victor_string'] = '"Who lives in a pineapple under the sea? SpongeBob SquarePants! Absorbent and yellow and porous is he. SpongeBob SquarePants! If nautical nonsense be something you wish. SpongeBob SquarePants! Then drop on the deck and flop like a fish! SpongeBob SquarePants!"'

string_one = 'abcd'

# make new variable that equals an re.compile() on your string.
my_compile = re.compile(string_one)

print(my_compile)

my_match = my_compile.match('abcd123')

print(my_match)

my_findall = my_compile.findall('123abcd abcd123 abcd abcabc acb')

print(f'findall example: {my_findall}')

mark_compile = re.compile('comedy')

mark_findall = mark_compile.findall(string_dict['mark_string'])

print(mark_findall)
print(len(mark_findall))

mark_match = mark_compile.match(string_dict['mark_string'])

print(mark_match)

mark_search = mark_compile.search(string_dict['mark_string'])
print(mark_search)

# print(f'string_dict: {string_dict}')



#[a-z] or [A-Z]: these sets capture all letters for their case
#[^2]

pattern_int = re.compile('[0-7][7-9][0-3]')

print(pattern_int)

my_var = pattern_int.search('67383')

print(my_var)
print(my_var.span())



#Group Exercise # 1:
#Use the search(), findall(), and match() methods on one of the strings we wrote.

chris_string = string_dict['christopher_string']
print(chris_string)



my_pattern = re.compile('[A-Z]').search(string_dict['george_string'])
print(my_pattern)

#find any character with regex, letter, 
pattern_1 = re.compile('[\w]+')

test_1 = pattern_1.findall(string_dict['george_string'])
print(test_1)

pattern_2 = re.compile('\d')

test_2 = pattern_2.findall(string_dict['juneun_string'])
print(test_2)

my_string = string_dict['jessica_string']
print(my_string)

name_pattern = re.compile('([A-Z][a-z]+) ([A-Z][a-z]+)')

find_names = name_pattern.findall(my_string)
print(find_names)

print(f'my_string: {my_string}')

for name in my_string.split(','):
    print(name)

    match = re.compile('[A-Z]').search(name)

    if match:
        print(match.groups(1))

    else:
        print('no match')

#for name in find_names:
   # print(name[0] + ' ' name[1])
emails = ['blue@gmail.com', 'green@gmail.com', 'red@gmail.com']

email_pattern = re.compile('([\w]+)@([a-z])(.com|.org)')
found_emails = email_pattern.findall(emails[0])
print(found_emails)

for i in range(3):
    found_emails = email_pattern.findall(emails[i])
    print(found_emails)



#Group Exercise #2: write a validator for Scottish names (e.g., "McDonald", "McFarland", etc.)

name = ['McDonald', 'McFarland', 'Revelette', 'Kulas']
print(name)
names_pattern = name
names_pattern = re.compile('([A-Z][a-z][A-Z])')


