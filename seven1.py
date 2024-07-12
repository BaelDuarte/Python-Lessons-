start_program = input('welcome to car rental calculator, want to start? (y/n): ')
if start_program == 'y':
    user_input1 = int(input('insert how many kilometers were driven: '))
    user_input2 = int(input('insert how many days you kept the car: '))
    print('you kept the car for {} days and drove {} kilometers, you will have to pay {:.3f} USD.'.format(user_input2, user_input1, user_input1*0.15+user_input2*60))
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')