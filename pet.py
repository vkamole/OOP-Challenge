class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Moderate hunger level
        self.energy = 5  # Moderate energy level
        self.happiness = 5  # Moderate happiness level

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} ate some food. Hunger decreased, happiness increased!")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} took a nap. Energy increased!")

    def play(self):
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} played with you. Energy decreased, happiness increased, hunger slightly increased!")

    def get_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {'◼' * self.hunger}{'◻' * (10 - self.hunger)} ({self.hunger}/10)")
        print(f"Energy: {'◼' * self.energy}{'◻' * (10 - self.energy)} ({self.energy}/10)")
        print(f"Happiness: {'◼' * self.happiness}{'◻' * (10 - self.happiness)} ({self.happiness}/10)")

# Example usage:
if __name__ == "__main__":
    my_pet = Pet("Fluffy")
    my_pet.get_status()
    
    my_pet.play()
    my_pet.get_status()
    
    my_pet.eat()
    my_pet.get_status()
    
    my_pet.sleep()
    my_pet.get_status()