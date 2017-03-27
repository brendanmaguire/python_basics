vowels = ('a', 'e', 'i', 'o', 'u')
print('There are {} vowels'.format(len(vowels)))

sentence = 'I eat apples in April' 
print('The vowels in "{}" are:'.format(sentence), end=' ')
for letter in sentence:
    # If the letter is in the vowel tuple
    if letter.lower() in vowels:
        print(letter, end=' ')

