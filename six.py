start_program = input('welcome to ultimate input analizer, want to start? (y/n): ')
if (start_program == 'y'):
    user_input = input('insert the input you want to analize: ')
    print('the input type is ', type(user_input))
    print('input is a number?', user_input.isnumeric()) 
    print('input is alphet?', user_input.isalpha())
    print('input is alphanumeric?' , user_input.isalnum())
    print('input is all capitalized?', user_input.isupper())
    print('input is in lowercase?', user_input.islower())
    print('input is capitalize?', user_input.istitle())
elif (start_program == 'n'):
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')