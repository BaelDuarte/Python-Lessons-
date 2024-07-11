start_program = input('welcome to ultimate 15% pay rise calculator, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert your current salary: '))
    print('your current salary is {}, with 15% of pay rise, now it goes to {}'.format(user_input, user_input/100*15))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')