import time

print('Countdown...')

time_left = 3
while time_left > 0:
    print('{}..'.format(time_left))
    time_left = time_left - 1
    time.sleep(1)

print('Take off!!')

