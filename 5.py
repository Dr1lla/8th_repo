class Pet:
    total = 0

    @staticmethod
    def status():
        print("Загальна кількість звірят", Pet.total)

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        Pet.total += 1

    def talk(self):
        print("Привіт, я звірятко, мене звати", self.name)    

    def __str__(self):
        ans = "Об'єм класу Pet\n"
        ans += "ім'я: " + self.name + "\n"
        return ans

def main():
    print('Доступ до атрибуту класу Pet.total', end=" ")
    print(Pet.total)

    print("Створення звірят")
    pet1 = Pet('Бобік')
    pet1.talk()
    pet2 = Pet('Мурзік')
    pet2.talk()
    pet3 = Pet('Кеш')
    pet3.talk()

    Pet.status()

    print("Доступ до атрибуту класу через об'єкт:", end= " ")
    print(pet1.total)

main()