class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def movement(self):
        print("Moves from one place to another")


class Bird(Animal):
    def __init__(self):
        super().__init__()

    def movement(self):
        super().movement()
        print("While flying!")

    def breathe(self):
        print("Inhales and Exhales")

jake = Bird()
jake.movement()
jake.breathe()
print(jake.num_of_eyes)