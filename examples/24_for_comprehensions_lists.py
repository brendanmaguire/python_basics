numbers = [3,9,2,1,10,4,2,7]

# Transform - Get the squares
squares = [v * v for v in numbers]

# Filter - Only keep the even numbers
evens = [v for v in numbers if v % 2]

print(squares)
print(evens)

