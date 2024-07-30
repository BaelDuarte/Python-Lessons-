start_program = input('welcome to ultimate multiplication table indicator, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the number you want to multiply: '))
    print('the multiplication table of {} is {},{},{},{},{},{},{},{},{},{}'.format(user_input, user_input*1, user_input*2, user_input*3, user_input*4, user_input*5, user_input*6, user_input*7, user_input*8, user_input*9, user_input*10))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')