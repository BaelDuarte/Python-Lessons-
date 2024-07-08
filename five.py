# sourcery skip: use-fstring-for-formatting
start_program = input('welcome to ultimate two numbers summator v0.1, want to start? (y/n): ')
if (start_program == 'y'):
    first_number = int(input('insert the first number: '))
    second_number = int(input('insert the second number: '))
    result = first_number + second_number
    print('the result between {} and {} is: {}'.format(first_number, second_number, result))
elif (start_program == 'n'):
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')