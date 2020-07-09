hatList = [1, 2, 3, 4, 5,6]  # This is an existing list of numbers hidden in the hat.

# get the middle of a list

def getMiddle(list):
    if( len(list) % 2 != 0):
        print("cool:",len(list)/2)
        middle = (int(len(list)/2))-1
    middle = int(len(list)/2)
    return middle

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
num = int(input("Please enter a number"))
mid_indx = getMiddle(hatList)
hatList[mid_indx] = num

# Step 2: write a line of code here that removes the last element from the list.
del hatList[len(hatList)-1]

# Step 3: write a line of code here that prints the length of the existing list.
print("lenght of this list", len(hatList))

print(hatList)

# 3.1.4.12

myList = [1,2,3,4,5,6,7,8,9,10,11]

for i in range(len(myList)//2):
    print("i, ", i)
    j = len(myList)-i-1
    print("j, ", j)
    myList[i], myList[j] = myList[j], myList[i]

print(myList)

# 3.1.4.13

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.extend(["j", "p","g"])
print("Step 2:", beatles)

# step 3
print("Step 3:", beatles)
for i in range(2):
    member = input("please give a name: ")
    beatles.append(member)

# step 4
print("Step 4:", beatles)
if "s" in beatles: beatles.remove("s")
del beatles[-1]

# step 5
print("Step 5:", beatles)
beatles.insert(0, "r")


# testing list legth
print("The Fab", len(beatles))
