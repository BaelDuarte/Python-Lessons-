start_program = input('welcome to ultimate double, triple and square root indicator, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the number you want to compare: '))
    print('the double of {} is {}, your triple is {}, and your square root is {:.3f}'.format(user_input, user_input*2, user_input*3, user_input**(1/2)))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')