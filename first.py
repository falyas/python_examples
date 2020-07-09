# 2.1.6.9
# input a float value for variable a here
a = input("Please enter a float: ")
# input a float value for variable b here
b = input("Please enter another float: ")
# convert from strings to floats
a = float(a)
b = float(b)

# output the result of addition here
print(a+b)
# output the result of subtraction here
print(a-b)
# output the result of multiplication here
print(a*b)
# output the result of division here
print(a/b)

print("\nThat's all, folks!")

# 2.1.6.10

x = float(input("Enter value for x: "))

# put your code here

y = 1/(x+1/(x+(1/(x+(1/x)))))

print("y =", y)

# 2.1.6.11
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
dura_hours = int(dura/60)
dura_mins = ((dura/60) - dura_hours)*60

final_mins = mins + dura_mins

while(final_mins > 60):
    final_mins -= 60
    dura_hours += 1

final_hours = hour + dura_hours

while(final_hours > 24):
    final_hours -=24

print(int(final_hours), ":", int(final_mins), sep="")

# 3.1.1.12
income = float(input("Enter the annual income: "))

#
# Put your code here.
#

if income < 85528:
    tax = (income * 0.18) - 556.2
else:
    tax = 14839.2 + ((income-85528)*0.32)

if tax < 0:
    tax = 0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")

# 3.1.2.10

# Prompt the user to enter a word
# and assign it to the userWord variable.

#Approach 1
userWord = input("Please enter a word: ")
userWord = userWord.upper()

vowels = ['A', 'E', 'I', 'O', 'U']
for letter in userWord:
    # Complete the body of the for loop.
    if letter not in vowels:
        print(letter)

# 3.1.2.11
wordWithoutVovels = ""

# Prompt the user to enter a word
# and assign it to the userWord variable
userWord = input("Enter a word: ").upper()

#Approach 1
vowels = ['A', 'E', 'I', 'O', 'U']
for letter in userWord:
    # Complete the body of the for loop.
    if letter not in vowels:
        print(letter, end='')

print("\n-----------")
#Approach 2
# Print the word assigned to wordWithoutVowels.
for letter in userWord:
    if letter not in vowels:
        wordWithoutVovels += letter

print(wordWithoutVovels)

# 3.1.2.14

import math

blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#

### Approach 1
### Let's build the pyramid from the top to bottom
### Each time we use a block we will decrement the number of blocks
### If the number of blocks left supports the minimum blocks needed for a layer
### then we'll continue building, otherwise we'll stop and return
### and throughout the program we would have to count the height
### This approach runs in O(n) time where n is the number of blocks

height = 0
next_blocks_layer = 1

while(blocks >= next_blocks_layer):
    # notice that the order of 'blocks -= next_blocks_layer'
    # and 'next_blocks_layer+=1' is important for the program to give correct results
    blocks -= next_blocks_layer
    height += 1
    next_blocks_layer += 1

# separater
print("-------")

### Failed, but okay attempt because I aimed to improve efficiency
### By observation, this pyramid adheres to the shape
### structure of the balanced binary search tree
### with n nodes, in which the nodes can be thought of as blocks
### and the height of the balanced binary tree is log_2(n)
### this same idea can be used to calculate the height of the pyramid
### We would have to take into consideration that the number of blocks
### doesn't always complete a level, by taking off the number of blocks
### that form an incomplete level. I don't know how to get that number of
### blocks since the number of blocks depends on the hieght - and we
### want to get the height - so ...

# if(blocks > 0):
    # height = math.log2(blocks)

print("The height of the pyramid:", height)

# 3.1.2.15

#This program shows Lothar Collatz hypothesis:
# A whole number goes to zero using algm and 3x+1 equation
c0 = int(input("Enter a non-zero and positive number: "))

steps = 0
while(c0 != 1 and c0 > 0):
    if (c0 % 2 == 0):
        c0 /= 2
        steps +=1
        print(int(c0))
    else:
        c0 = 3 * c0 + 1
        steps +=1
        print(int(c0))

print("steps: ", steps)

# 
