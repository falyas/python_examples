def fun(a):
    if a > 30:
        return 3
    else:
        print(a)
        return a + fun(a + 3)

print(fun(25))

# example of a dictionary with a list of values for the key

school_class = {}

while True:
    name = input("Enter the student's name (or type exit to stop): ")
    if name == 'exit':
        break
    
    score = int(input("Enter the student's score (0-10): "))
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
    
 # d3 from d1 and d2

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

# you can convert sequences into tuples

l = ["car", "Ford", "flower", "Tulip"]

t = tuple(l)
print(t)

# you can also convert a key-value pairs of a sequence into a dictionary
colors = (("green", "#008000"), ("blue", "#0000FF"))

# convert tuple to dictionary - approach 1 - think about the cons for this approach .  .  .
colDict = {}
for item in colors:
    if item not in colDict.keys():
        colDict[item[0]] = item[1]

# convert tuple to dictionary - approach 2
colDict = dict(colors)

print(colDict)

# The items method returns a tuple of the key value pairs inside the dictionary

colors = {
    "white" : (255, 255, 255),
    "grey"  : (128, 128, 128),
    "red"   : (255, 0, 0),
    "green" : (0, 128, 0)
    }

for col, rgb in colors.items():
    print(col, ":", rgb)
