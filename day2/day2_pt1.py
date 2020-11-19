data = open("input.txt", "r")
gift_wrap_required = 0
for dimensions in data:
    dim = list(map(lambda x : int(x), dimensions.rstrip().split('x')))
    surface_areas = [dim[0] * dim[1], dim[1] * dim[2], dim[0] * dim[2]]
    gift_wrap_required += (2 * sum(surface_areas)) + min(surface_areas)
print(gift_wrap_required)

