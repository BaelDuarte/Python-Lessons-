import playsound
start_program = input('welcome to play a sound!, want to start? (y/n): ')
if start_program == 'y':
    user_input = input('insert the path MP3 file: ')
    playsound('Este computador/Área de Trabalho/Tudo/Audios')
elif start_program == 'n':
    print('ok, shutting down the program...')
else:
    print('invalid format, shutting down the program...')