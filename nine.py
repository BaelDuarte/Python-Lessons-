start_program = input('welcome to school grade analyzer, want to start? (y/n) >>OBS: just works for two grades XD<< : ')
if start_program == 'y':
    first_grade = int(input('insert the first grade: '))
    second_grade = int(input('insert the second grade: '))
    print('the the average between the two grades is {}'.format((first_grade + second_grade) / 2))
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')