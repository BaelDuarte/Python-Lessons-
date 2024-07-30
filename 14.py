start_program = input('welcome to 5% off calculator, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the number you want to be calculated: '))
    print('the original value is {}, with 5% off, goes to {}'.format(user_input, user_input*0.05))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')