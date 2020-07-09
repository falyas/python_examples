# 3.1.6.9

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
newList = []
for i in myList:
    if i not in newList:
        newList.insert(0,i)

print("The list with unique elements only:")
print(newList)
