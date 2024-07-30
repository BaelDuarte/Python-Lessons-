from math import sin,cos,tan
start_program = input('welcome to ultimate XX sine, cosine and tanguent ultra calculator, want to start? (y/n): ')
if start_program == 'y':
    user_input = float(input('insert the angle you want to calculate: '))
    print('the sine of {:.0f} is {:.2f}, your cosine is {:.2f} and your tanguent is equivalent to {}'.format(user_input, sin(user_input), cos(user_input), tan(user_input)))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')