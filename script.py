def main():
    class Warrior:
        def __init__(self, name, health, power):
            self.name = name
            self.health = health
            self.power = power
        
        def status(self):
            print(f"{self.name}: {self.health} health and {self.power} power.")
        
        def attackedBy(self, other):
            self.health -= other.power
            print(f"\n{other.name} did {other.power} damage to {self.name}")

        def alive(self):
            if self.health <= 0:
                print(f"{self.name} died")
                return True
            else:
                return False

    hero = Warrior("You", 10, 5)
    goblin = Warrior("Goblin", 6, 2)

    class Zombie(Warrior):
        def __init__(self, name, power):
            self.name = name
            self.power = power 

    zombie = Zombie("Zombie", 3)

    status = False
    while (status == False):
        hero.status()
        goblin.status()
        user_choice = input("\nWhat do you want to do?\n1: Fight goblin\n2: Do nothing\n3: Flee\n4: Zombie?\nType 1, 2, 3, or 4: ")
        if user_choice == '1':
            goblin.attackedBy(hero)
            status = goblin.alive()
        elif user_choice == '2':
            hero.attackedBy(goblin)
            status = hero.alive()
        elif user_choice == '3':
            print("Goodbye!")
            break
        elif user_choice == '4':
            hero.attackedBy(zombie)
            print("Zombies cannot die!")
            status = hero.alive()
        else:
            print("*** ERROR: Not a valid selection. Try again ***")

main()