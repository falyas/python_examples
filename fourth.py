int_list2=[]
n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", a)

for i in a:
    if i>=0:
        int_list2.append(i)

# Bubble sort, which sorts in ascending
swap = True
while swap == True:
    swap=False
    for i in range(len(int_list2)-1):
        #swapping here
        if int_list2[i] > int_list2[i+1]:
            swap=True
            tmp = int_list2[i]
            int_list2[i] = int_list2[i+1]
            int_list2[i+1] = tmp

# remove the negative values from the list after it has been sorted
print("The sorted list is: ", int_list2)
