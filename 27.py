#escreva um codigo que leia o nome de uma cidade e retorne se a ciudade comeca ou nao com 'santo'

# sourcery skip: simplify-boolean-comparison

city_name = input('insert the city name: ')
checker = 'Santo' in city_name
if checker == True:
    print('the city`s name starts with Santo')
else:
    print('the city name doesn`t start with Santo')

'''city_name = input('insert the city name: ')
city_name = city_name.split
first_name = city_name[0]
checker = 'Santo' in first_name
if checker == True:
    print('the city`s name starts with Santo')
else:
    print('the city name doesn`t start with Santo')'''