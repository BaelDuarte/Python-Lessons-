start_program = input('welcome to BRR to USD converter, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the value you want to convert: '))
    print('the conversion of BRR {:.2f} to USD is {:.2f}'.format(user_input, user_input/5.41))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')