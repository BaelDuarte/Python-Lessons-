start_program = input('welcome to celsius to fahrenheit converter, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the temperature in Celsius: '))
    print('{} degrees Celsius is equivalent to {:.2f} Fahrenheit'.format(user_input, user_input*1.8+32))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')