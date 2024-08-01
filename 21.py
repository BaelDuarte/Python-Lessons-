import math
start_program = input('welcome to ultimate XX sine, cosine and tanguent ultra calculator, want to start? (y/n): ')
if start_program == 'y':
    user_input = float(input('insert the angle you want to calculate: '))
    print('the sine of {:.0f} is {:.2f}'.format(user_input, math.sin(math.radians(user_input))))
    print('your cosine is {:.2f}'.format(math.cos(math.radians(user_input))))
    print('and your tanguent is equivalent to {:.2f}'.format(math.tan(math.radians(user_input))))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')