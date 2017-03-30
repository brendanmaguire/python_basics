word = input('Enter your word: ')

if word[0].lower() != 't':
    print('The word "{}" does not start with "t"'.format(word))
elif len(word) < 3:
    print('The word "{}" is too short'.format(word))
elif len(word) > 6:
    print('The word "{}" is too long'.format(word))
else:
    print('The word "{}" satisfies this program!'.format(word))
