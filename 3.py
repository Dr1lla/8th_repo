class Pet:
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    def talk(self):
        print("Привіт, я звірятко, мене звати ", self.name)

def main():
    pet1 = Pet('Бобік')
    pet1.talk()
    pet2 = Pet('Мурзік')
    pet2.talk()
    print('Доступ до атрибуту -', pet1.name)

main()