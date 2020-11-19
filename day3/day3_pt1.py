directions = open('input.txt', 'r').read()
visited_houses = {'0,0'}
current_position = [0, 0] # [x, y] coordinates
for direction in directions:
    if direction == '^':
        current_position[1] += 1
    elif direction == 'v':
        current_position[1] -= 1
    elif direction == '>':
        current_position[0] += 1
    elif direction == '<':
        current_position[0] -= 1
    else:
        print("invalid direction")
    visited_houses.add("{x},{y}".format(x=current_position[0], y=current_position[1]))
print(len(visited_houses))        
