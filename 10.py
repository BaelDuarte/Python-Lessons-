start_program = input('welcome to meter converter, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the measure you want to convert in meters: '))
    print('the measure {} meters converted to centimeters is {}, and for milimeters is {}'.format(user_input, user_input*100, user_input*1000))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')