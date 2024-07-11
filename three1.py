start_program = input('welcome to >>how much ink calculator<<, want to start? (y/n): ')
if start_program == 'y':
    user_input = int(input('insert the heigh of your wall in meters: '))
    user_input2 = int(input('insert the width of your wall in meters: '))
    user_area = user_input*user_input2
    print('the area of your wall is about of {}, each liter of ink paint just 2M^2, so you need {} liters of ink.'.format(user_area, user_area/2))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')