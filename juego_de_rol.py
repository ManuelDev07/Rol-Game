'''
Juego de Rol:
1) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que reduzca la vida según una cantidad 
recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover que reciba una dirección y se mueva en esa dirección la cantidad 
indicada por velocidad.

2) Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro personaje, al que le debe hacer 
el daño indicado por el atributo ataque.

3) Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que devuelva la cantidad cosechada.
'''
class Personaje:
    def __init__(self, name, life, position, speed):
        self.name = name
        self.life = life
        self.position = position
        self.speed = speed

    def get_damage(self, damage):
        while True:

            if self.position == "defensa":
                return print(f"{self.name} se ha defendido!.\n")

            elif self.position == "ataque" or "mover":
                print(f"{self.name} ha perdido -{damage}pts de vida.\n")
                self.life -= damage
                
                if self.life <= 0:
                    return f"{self.name} ha sido derrotado...\n"

                else:
                    return f"{self.life}pts de vida restantes para {self.name}.\n"

            break

    def move(self, direction):

        if self.position == "mover":
            print(f"Se ha movido a la {direction} {self.speed} pasos.\n")

        elif self.position == "defensa":
            print(f"{self.name} no se puede mover, está en posición de Defensa.\n")

        elif self.position == "ataque":
            print(f"{self.name} está en posición de Ataque por lo que se moverá {self.speed // 2} pasos.\n")

        else:
            print("ERROR!")

    def __str__(self): #opcional
        return f"Tu personaje: {self.name} ha sido creado! :D"



class Soldado(Personaje):
    def __init__(self, name, life, position, speed, atk):
        super().__init__(name, life, position, speed)
        self.atk = atk

    def attack(self, character):
        if self.position == "ataque":
            print(f"{self.name} ha hecho {self.atk}pts de daño a {character.name}. \n")
            print(character.get_damage(self.atk))



class Campesino(Personaje):
    def __init__(self, name, life, position, speed, harvest_ability):
        super().__init__(name, life, position, speed)
        self.harvest_ability = harvest_ability

    def harvest(self, quant):
        if self.position == "cosechar":
            return f"La cantidad cosechada de Trigo({quant}) por {self.name} más su bonus de Habilidad es de: {self.harvest_ability * quant}.\n"
        
        else:
            return "No puedes Cosechar..."