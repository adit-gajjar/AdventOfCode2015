directions = open('input.txt', 'r').read()
floor = 0
for direction in directions:
    floor += 1 if direction == '(' else -1
print(floor)
