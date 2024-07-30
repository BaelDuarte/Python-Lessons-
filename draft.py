start_program = input('welcome to [...], want to start? (y/n): ')
if start_program == 'y':
    user_input = input('')
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')