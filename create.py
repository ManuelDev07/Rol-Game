#Creación de Personaje:
from juego_de_rol import Personaje, Soldado, Campesino

def create_character():
    '''Función que permitirá al usuario crear su propio personaje(obj).'''

    print("Elegir clase: (Soldado / Campesino)")
    character = input('>>>').lower()

    if character == "soldado":
        try:
            for player in range(2):
                print("Ingrese sus Atributos:")
                name = input("Nombre: ")
                life = int(input('Vida: '))
                position = input("Estado (Defensa,Ataque o Mover): ")
                speed = int(input("Velocidad: "))
                atk = int(input("Ataque: "))
                player = Soldado(name, life, position, speed, atk)

        except ValueError:
            print('ERROR')

    elif character == "campesino":
        try:
            print("Ingrese sus Atributos:")
            name = input("Nombre: ")
            life = int(input('Vida: '))
            position = input("Estado (Neutral, Mover o Cosechar): ").lower()
            speed = int(input("Velocidad: "))
            harvest_ability = int(input("Habilidad de Cosecha: "))
            print(Campesino(name, life, position, speed, harvest_ability))

        except ValueError:
            print('ERROR')
            
    else: 
        print("ERROR! Clase Inexistente")
