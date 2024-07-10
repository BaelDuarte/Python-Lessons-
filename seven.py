start_program = input('welcome to predecessor and successor indicator, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the number you want to compare: '))
    print('the predecessor of {} is {}, and your sucessor is {}'.format(user_input, user_input-1, user_input+1))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')