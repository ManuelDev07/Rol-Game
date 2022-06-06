#Gameplay:

from calendar import c
import random
from juego_de_rol import Personaje, Soldado, Campesino


def play_game():
    '''Función que se encargará del gameplay, los turnos y las llamadas a la clase para sus métodos'''
    
    print(f'''
{'-'*110}
Recuerda:
{'-'*110}
-Si eres Soldado sólo podrás moverte, atacar o defenderte.
-Si eres Campesino sólo podrás moverte o cosechar.
{'-'*110}

{'-'*110}
Indicaciones:
{'-'*110}
-Puedes escoger el modo de juego ["Solitario" (vs. PC) u "Otro" (PvP)]
-Y la dificultad para el juego [Facil: 6 turnos | Intermedio: 16 Turnos | Difícil: 26 turnos | BOSS: 70 Turnos]
{'-'*110}
''')
    print("Modo de juego:")
    mode = input('>>>').lower()
    print("\nDificultad:")
    rounds = input(">>>").lower()

    if mode == "otro":
        if rounds == 'facil':
            for turno in range(6):
                do = input("¿Que Hará? ")
                if do == 'atacar':
                    Soldado.attack()