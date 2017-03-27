words = ['sign', 'apple', 'baloon', 'dog', 'ball', 'sweet']

# Create a map with a letter as key and the last word in the list
# starting with that letter
last_found = { w[0]: w for w in words }
print(last_found)

