class Television:
    def __init__(self, max_channel=100, max_volume=50):
        self.channel = 1  # Поточний канал
        self.volume = 10  # Поточний рівень гучності
        self.max_channel = max_channel
        self.max_volume = max_volume

    def set_channel(self, channel):
        if 1 <= channel <= self.max_channel:
            self.channel = channel
            print(f"Канал змінено на {self.channel}")
        else:
            print(f"Канал має бути в межах 1-{self.max_channel}.")

    def increase_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
            print(f"Гучність збільшено: {self.volume}")
        else:
            print("Гучність вже на максимальному рівні!")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1
            print(f"Гучність зменшено: {self.volume}")
        else:
            print("Гучність вже на мінімальному рівні!")

    def __str__(self):
        return f"Телевізор: канал {self.channel}, гучність {self.volume}"


# Основна програма
tv = Television()

while True:
    print("\n--- Меню телевізора ---")
    print("1. Змінити канал")
    print("2. Збільшити гучність")
    print("3. Зменшити гучність")
    print("4. Показати стан телевізора")
    print("5. Вийти")

    choice = input("Ваш вибір: ").strip()
    if choice == "1":
        try:
            new_channel = int(input("Введіть номер каналу: "))
            tv.set_channel(new_channel)
        except ValueError:
            print("Введіть коректний номер каналу!")
    elif choice == "2":
        tv.increase_volume()
    elif choice == "3":
        tv.decrease_volume()
    elif choice == "4":
        print(tv)
    elif choice == "5":
        print("Вихід з програми.")
        break
    else:
        print("Невірний вибір! Спробуйте знову.")