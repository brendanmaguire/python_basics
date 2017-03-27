def add(x, y, z):
    return x + y + z

print(add(1, 2, 3))

# x is passed implicitly; y & z are passed explicitly
print(add(1, z=7, y=3))

