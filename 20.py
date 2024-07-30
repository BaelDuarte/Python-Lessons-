from math import hypot
start_program = input('welcome to ultimate hypotenuse calculator, want to start? (y/n): ')
if start_program == 'y':
    user_input = float(input('insert the opposite cateto: '))
    user_input2 = float(input('insert the adjacent cateto:'))
    print('the value of the hypotenuse is {:.2f}'.format(hypot(user_input, user_input2)))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')