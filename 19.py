from math import floor
start_program = input('welcome to integer part analyzer, want to start? (y/n): ')
if start_program == 'y':
    user_input = float(input('insert a number: '))
    print('the integer part of {} is {}'.format(user_input,floor(user_input)))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')




