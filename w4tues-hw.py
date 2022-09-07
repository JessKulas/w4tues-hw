import re

with open("names.txt") as text: #names.txt should be in your project folder for your homework
    data = text.readlines()

for item in data:
   print(item)

# Generate the desired output. Hint: use an asterisk * in your re.compile()

# Output:
# Abraham Lincoln
# Andrew P Garfield
# Connor Milliken
# Jordan Alexander Williams
# None
# None


string_dict = {}
string_dict['emails'] = 'Hawkins, Derek derek@codingtemple.com	(555) 555-5555	Teacher, Coding Temple	@derekhawkins Zhai, Mo	mozhai@codingtemple.com	(555) 555-5554	Teacher, Coding Temple Johnson, Joe	joejohnson@codingtemple.com	 Johson, JoeOsterberg, Sven-Erik	governor@norrbotten.co.se Governor, Norrbotten @sverik, Tim tim@killerrabbit.com  Enchanter, Killer Rabbit Cave Butz, Ryan	ryanb@codingtemple.com	(555) 555-5543	CEO, Coding Temple	@ryanbutz Doctor, The doctor+companion@tardis.co.uk	Time Lord, Gallifrey Exampleson, Example	me@example.com	555-555-5552	Example, Example Co. @example Pael, Ripal ripalp@codingtemple.com	(555) 555-5553	Teacher, Coding Temple	@ripalp Vader, Darth	darth-vader@empire.gov	(555) 555-4444	Sith Lord, Galactic Empire	@darthvader Fernandez de la Vega Sanz, Maria Teresa	mtfvs@spain.gov	 First Deputy Prime Minister, Spanish Gov'

my_string = string_dict['info']
print(my_string)

name_pattern = re.compile('([A-Z][a-z]+) ([A-Z][a-z]+)')

find_names = name_pattern.findall(my_string)
print(find_names)

print(f'my_string: {my_string}')

for name in my_string.split(','):
    print(name)

emails = ['blue@gmail.com', 'green@gmail.com', 'red@gmail.com']

email_pattern = re.compile('([\w]+)@([a-z])(.com|.org)')
found_emails = email_pattern.findall(emails[0])
print(found_emails)

for i in range(3):
    found_emails = email_pattern.findall(emails[i])
    print(found_emails)