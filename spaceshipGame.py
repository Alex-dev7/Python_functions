import random


# Class Ship defines the basic attributes and behaviors of a ship
class Ship:
    
     # Initialize the ship with hull, firepower, and accuracy
    def __init__(self, hull, firepower, accuracy):
        self.hull = hull
        self.firepower = firepower
        self.accuracy = accuracy

     # Attack another ship by subtracting the firepower from its hull
    def attack(self, other_ship):
        if random.random() <= self.accuracy:
            print(f"{self} hits {other_ship} with {self.firepower} firepower")
            other_ship.hull -= self.firepower
            if other_ship.hull <= 0:
                print(f"{other_ship} has been destroyed!")
        else:
            print(f"{self} misses the attack!")

    # Represent the ship object as its class name
    def __repr__(self):
        return self.__class__.__name__


# Subclass of Ship
class USS_Schwarzenegger(Ship):
    def __init__(self):
        # Call the  dunder __init__ method of the parent class Ship to set the values for hull, firepower, and accuracy
        super().__init__(20, 5, 0.7)

# Subclass of Ship
class Alien_Ship(Ship):
    def __init__(self):
        # Call the  dunder __init__ method of the parent class Ship to set the values for hull, firepower, and accuracy
        # Give them random values
        super().__init__(random.randint(3, 6), random.randint(2, 4), random.uniform(0.6, 0.8))

class Game:
    def __init__(self):
        self.uss_schwarzenegger = USS_Schwarzenegger()
        self.alien_ships = [Alien_Ship() for i in range(random.randint(1, 6))]
        self.current_ship = self.alien_ships[0]

     # The main game loop
    def play(self):
        while self.uss_schwarzenegger.hull > 0 and self.alien_ships:
            self.uss_schwarzenegger.attack(self.current_ship)
            if self.current_ship.hull <= 0:
                self.alien_ships.remove(self.current_ship)
                if self.alien_ships:
                    self.current_ship = self.alien_ships[0]
            else:
                self.current_ship.attack(self.uss_schwarzenegger)
        if self.uss_schwarzenegger.hull <= 0:
            print("Game over, USS_Schwarzenegger has been destroyed!")
        else:
            print("You have successfully destroyed all the alien ships!")

Game().play()