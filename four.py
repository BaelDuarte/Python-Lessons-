# sourcery skip: use-fstring-for-concatenation
start_celebrate = input('welcome to birthday celebrator, want to start? (y/n): ')
if (start_celebrate == 'y'):
    day_birth = input('insert your birth date (day): ')
    month_birth = input('insert your birth date (month): ')
    year_birth = input('insert your birth date (year): ')
    print('you were bornt on ' +  month_birth ,  day_birth + ',' , year_birth )
elif (start_celebrate == 'n'):
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')

    

