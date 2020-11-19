data = open("input.txt", "r")
ribbon_required = 0
for dimensions in data:
    dim = list(map(lambda x: int(x), dimensions.rstrip().split('x')))
    perimeters = [2*(dim[0]+dim[1]), 2*(dim[1]+dim[2]), 2*(dim[0]+dim[2])]
    volume = dim[0]*dim[1]*dim[2]
    ribbon_required += min(perimeters) + volume
print(ribbon_required)
