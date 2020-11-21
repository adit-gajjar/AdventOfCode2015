directions = open('input.txt', 'r').read()
visited_houses = {'0,0'}
# [x, y] coordinates, santa and robo santa position
current_positions = [[0, 0], [0, 0]]
santas_turn = True
for direction in directions:
    current_position = current_positions[0] if santas_turn else current_positions[1]
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
    santas_turn = not santas_turn
print(len(visited_houses)) 
