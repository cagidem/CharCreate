from random import *
entry1 = input("Enter your character name: ")

class Character(object):
    def __init__(self, name, hp, damage, speed):
        self.name=name
        self.hp=hp
        self.damage=damage
        self.speed=speed
    def stats(self):
        print("Your Name: " + str(self.name))
        print("Your Health: " + str(self.hp))
        print("Your Damage: " + str(self.damage))
        print("Your Speed: " + str(self.speed))

def char_creation():
    entry_hp = input("Health: ")
    entry_damage = input("Damage: ")
    entry_speed = input("Sped: ")
    if int(entry_hp) == abs(int(entry_hp)) and int(entry_speed) == abs(int(entry_speed)) and int(entry_damage) == abs(int(entry_damage)):
        if (int(entry_hp) + int(entry_speed) + int(entry_damage)) == 100:
            my_char = Character(entry1, entry_hp, entry_damage, entry_speed)
            print("")
            print("Your character has been created!!")
            my_char.stats()
            return
        else:
            print("Your sum of stats should be 100.")
            return char_creation()
    else:
        print("Your stats cannot be negative!!")
        return char_creation()
        
def random_character():
    total = 100
    random_hp = randint(0,100)
    random_damage = randint(0,(total - random_hp))
    random_speed = total - random_hp - random_damage
    my_char = Character(entry1, random_hp, random_damage, random_speed)
    print("")
    print("Your character has been created!!")
    my_char.stats()
    return

def creation_check():
    entry2 = input("How do you want to create your character?: (random/myself) ")
    if str(entry2).lower() == "random":
        random_character()

    elif str(entry2).lower() == "myself":
        print("Pick your stats(health, damage and speed). Your sum of stats should be 100.")
        char_creation()
    else:
        print("Please select random or myself!!")
        return creation_check()
creation_check()
