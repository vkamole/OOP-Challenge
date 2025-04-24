class Pet:
    def _init_(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5

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

def main():
    # Create a pet
    my_pet = Pet("Buddy")
    
    # Initial status
    print("=== Initial Status ===")
    my_pet.get_status()
    
    # Test eating
    print("\n=== Testing eat() ===")
    my_pet.eat()
    my_pet.get_status()
    
    # Test playing
    print("\n=== Testing play() ===")
    my_pet.play()
    my_pet.get_status()
    
    # Test sleeping
    print("\n=== Testing sleep() ===")
    my_pet.sleep()
    my_pet.get_status()

 # Test multiple actions
    print("\n=== Testing multiple actions ===")
    my_pet.play()
    my_pet.play()
    my_pet.eat()
    my_pet.sleep()
    my_pet.get_status()

if __name__ == "__main__":
    main()