import random

class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.tiredness = 0
        self.happiness = 0
        self.alive = True

    def play(self):
        self.tiredness -= 1
        self.happiness += 2
        self.hunger -= 1

    def sleep(self):
        self.tiredness += 2
        self.hunger -= 0.3

    def eat(self):
        self.happiness += 1
        self.hunger += 1
        self.tiredness += 0.2

    def is_alive(self):
        if self.hunger < -3:
            print("Umer potomu shto ne pozhral")
            self.alive = False
        elif self.tiredness < -5:
            print("USTAL i UMER")
            self,alive = False
        elif self.happiness < -4:
            print("Depression")
            self.alive = False

    def end_of_day(self):
        print(f"Happiness = {self.happiness}")
        print(f"Hunger = {self.hunger}")
        print(f"Tiredness ={self.tiredness}")

        def live (self, day):
            day = "Day " + str(day) + " of " + self.name + " life"
            print(f"{day:=^50}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.eat()
        elif live_cube == 2:
            self.sleep()
        elif live_cube == 3:
            self.play()
        self.end_of_day()
        self.is_alive()

pet = Cat(name="Sima")
for day in range(365):
    if pet.alive == False:
        break
    pet.live(day+1)
