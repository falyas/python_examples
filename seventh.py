# vacancy
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[2][14][0] = True
rooms[2][14][1] = True
rooms[2][14][2] = True

vacancy = 0

rooms = [[[0 for r in range(20)] for f in range(15)] for t in range(3)]

rooms[2][14][0] = True
rooms[2][14][1] = True
rooms[2][14][2] = True

vacancy = 0

for r in rooms[2][14]:
    if r is not True:
        vacancy += 1

print("vacacny count: ", vacancy)

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube[2][2][0]) # outputs: ':)'

print(cube[2][2][1]) # outputs: 'x'

# << operator
var = 1
while var < 10:
    print("#")
    print(var)
    var = var <<1

print(1 << 2)
