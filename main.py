import random as rm

names = ['keven', 'steve', 'george', 'spencer', 'reagan', 'ignacio', 'ahmed', 'ben', 'sophie', 'sebastian', 'juan', 'mia', 'kenny', 'michelle']
types = ['fire', 'water', 'plant', 'electricity']
healthrange = (40, 80)
attackrange = (20, 40)
pokemons = []

class Pokemon:

    def __init__(self, name, health, attack, type=None):
        self.name = name.capitalize()
        self.health = health
        self.__attack = attack
        self.type = type.lower()

        for t in types:
            if self.type == t:
                return
        print(f"unknown type when creating {self.name}")


    def attack(self, other):

        if self.health <= 0:
            print(f"{self.name} already fainted, cannot attack :(")
            return

        attackt = self.__attack

        if self.type == 'fire' and other.type == 'plant':
            attackt *= 2
        elif self.type == 'water' and other.type == 'fire':
            attackt *= 2
        elif self.type == 'plant' and other.type == 'electricity':
            attackt *= 2
        elif self.type == 'electricity' and other.type == 'water':
            attackt *= 2

        other.health -= attackt

        print(f"{self.name} attacked {other.name} with {attackt} damage {self.type} attack!")
        if other.health <= 0:
            print(f"{other.name} is fainted by {self.name} :(")
        else:
            print(f"{other.name} has {other.health} remaining!!")

    def __str__(self):
        return f"{self.name} is a {self.type} type pokemon with {self.health} health and {self.__attack} attack."


def createRandomPoke():
    randomName = names[rm.randint(0, len(names)-1)]
    names.remove(randomName)
    randomHealth = rm.randint(healthrange[0], healthrange[1])
    randomAttack = rm.randint(attackrange[0], attackrange[1])
    randomType = types[rm.randint(0, len(types)-1)]

    return Pokemon(randomName, randomHealth, randomAttack, randomType)

def main():
    for i in range(1, 5):
        newpoke = createRandomPoke()
        print(i, ". ", newpoke)
        pokemons.append(newpoke)

    select = int(input("Choose a pokemon to attack: ")) - 1
    templist = [x for x in range(len(pokemons)) if x != select]
    pokemons[select].attack(pokemons[templist[rm.randint(0, len(templist)-1)]])

main()

