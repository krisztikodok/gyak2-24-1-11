class Animal:
  def __init__(self,species):
    self.species=species
    print(f"This is a {self.species} species.")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(species="Dog") #call the constructor of the parent class(Animal) using super()
    self.name=name
    self.breed=breed
    print(f"{name} is a {self.breed}")

my_dog=Dog(name="Buddy",breed="Malamut")
your_dog=Dog(name="Blabber",breed="Wiener dog")

