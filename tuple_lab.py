# Coordinate unpacking
latitude, longitude = (17.385, 78.486)

# RGB unpacking
red, green, blue = (255, 128, 64)


x, y = 10, 20
# Before: x = 10, y = 20
x, y = y, x
# After: x = 20, y = 10


point = (2, 3)
new_point = (4,) + point[1:]
print(new_point)   # (4, 3)


# Original tuple
point = (2, 3)

# Convert tuple → list
point_list = list(point)

# Modify the list
point_list[0] = 4

# Convert list → tuple
new_point = tuple(point_list)

print(new_point)   # (4, 3)
