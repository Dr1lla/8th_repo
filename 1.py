class Pet:
    """Віртуальний вихованець"""

    def talk(self):
        print("Привіт, я звірятко.")

def main():
    pet = Pet()
    pet.talk()

main()