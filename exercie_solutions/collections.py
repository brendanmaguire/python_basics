words_str = input('Enter the words with white space separators: ')
words = words_str.split(' ')

word_length_map = {}

for word in words:
    word_len = len(word)

    if word_len not in word_length_map:
        word_length_map[word_len] = []

    word_length_map[word_len].append(word)

print(word_length_map)
