def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

def shout(phrase):
    if phrase == phrase.upper():
        return "YOU'RE SHOUTING!"
    else:
        return "Can you speak up?"

shout("I'M INTERESTED IN SHOUTING")


def cube(number):
    return number ** 3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

import math

print math.sqrt(25)


from math import sqrt

from module import *

import math
everything = dir(math)

print everything

def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

maximum = max(4423,54547,4324265467,11)
print maximum

minimum = min(21,34325,321,645365)
print minimum

absolute = abs(-213)

print type(50)
print type(3.5)
print type("fred")

def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

from math import sqrt

print sqrt(13689)

def distance_from_zero(absolute):
    if type(absolute) == int or type(absolute) == float:
        return abs(absolute)
    else:

        return "Nope"

print "Pig Latin"

original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = [1:len(new_word)]
    print original
else:
    print "empty"


pyg = 'ay'
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print new_word
else:

    print 'empty'


def answer():
    return 42

def hotel_cost(nights):
    return nights * 140


def planeride_cost(city):
    if city == "Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    elif city=="Pittsburgh":
        return 222
    elif city=="Los Angeles":
        return 475

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    return cost

def trip_cost(city,days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + planeride_cost(city) + spending_money

print trip_cost("Los Angeles", 5, 600)

zoo_animals = ["pangolin", "cassowary", "sloth", "LIOON" ];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

zoo_animals[3] = "bear"

suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shirts")
suitcase.append("shorts")
suitcase.append("pants")




list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]         # Third and fourth items (index two and three)
last   = suitcase[4:6]            # The last two items (index four and five)

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  =  animals[3:6]          # The fourth through sixth characters
frog =   animals[6:]       # From the seventh character to the end

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

duck_index = animals.index("duck")

animals.insert(5, "cobra")

my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print number * 2

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!

for number in start_list:
    square_list.append(number ** 2)
    square_list.sort()

print square_list



# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']


menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Steak'] = 10
menu['tomato'] = 4
menu['Jello'] =1



print "There are " + str(len(menu)) + " items on the menu."
print menu


# key - animal_name : value - location
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Rainforest Exhibit'

print zoo_animals


backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']

backpack.remove('dagger')


inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}mvds

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strangeberry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] += 50

names = ["Adam","Alex","Mariah","Martine","Columbus"]

for i in names:
    print i


webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for key in webster:
    print key

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
    if i % 2 == 0:
        print i

def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count++
    return count


for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter


