directions = open('input.txt', 'r').read()
floor = 0
num_directions = 1
for direction in directions:
    floor += 1 if direction == '(' else -1
    if floor == -1:
        break
    num_directions += 1
print(num_directions)
