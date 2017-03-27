while True:
    should_quit = input('Quit: [Y/n] ')
    if should_quit == 'Y':
        break

    user = input('Username: ')
    if len(user) == 0:
        continue

    print('Welcome, {}'.format(user))

