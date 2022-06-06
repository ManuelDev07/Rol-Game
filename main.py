#Menú de Juego:

from create import create_character
from play import play_game

def menu():
    '''Menú principal del juego, para crear, jugar o salir del programa'''
    
    print(f'''
\tMenú de Juego:
{'-'*100}
-Usar 1 para Crear Personaje.
-Usar 2 para Jugar.
-Usar 3 para Salir del juego.
{'-'*100}
''')
    while True:
        try:
            option = int(input('>>>'))
            if option == 1:
                create_character()
            
            elif option == 2:
                play_game()

            elif option == 3:
                break
            
            else:
                print('ERROR! Opción no disponible. Intente de nuevo... -_-')

        except ValueError:
            print('ERROR')


menu()