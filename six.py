start_program = input('welcome to ultimate two numbers summator v0.1, want to start? (y/n): ')
if (start_program == 'y'):
    first_number = input('insert the first number: ')
    second_number = input('insert the second number: ')
    result = int(first_number) + int(second_number)
    print('the result is:', result)
elif (start_program == 'n'):
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')