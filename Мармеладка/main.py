import random

print("1. Угадай число\n2. Загадай число\n3. Продублируй число\n4. Числа Пифагора\n5. Симулятор мармеладок\n")
zadanie = int(input("Введите номер задания: "))

if zadanie == 1:
    print("\nЗадание:\n Угадай число")
    a = random.randint(1, 10)
    number_try = 0
    print("Угадайте число от 1 до 10")
    while number_try <= 2:
        number_try += 1
        c = int(input("Введите число: "))
        if c > 10 or c < 1:
            print("Самый умный нашелся? Иди поспи...")
            exit()
        if c < a:
            print("Твое число меньше того, что БИБЛИОТЕКА ЗАГАДАЛА")
        if c > a:
            print("Твое число больше того, что БИБЛИОТЕКА ЗАГАДАЛА")
        if c == a:
            break
    if c == a:
        print("УХ ТЫ, ТЫ УГАДАЛ, БИБЛИОТЕКА ЗАГАДАЛА ЧИСЛО: ", a, "Попыток потрачено: ", number_try)
    else:
        print("!!!GAME OVER!!!\nУХ ТЫ, ТЫ НЕ УГАДАЛ, БИБЛИОТЕКА ЗАГАДАЛА ЧИСЛО: ", a)

if zadanie == 2:
    print("\nЗадание:\n Загадай число")
    number_try = 0
    print("Загадай число от 1 до 10")
    q = int(input("Введите загаданное число: "))
    if q > 10 or q < 1:
        print("Самый умный нашелся? Иди поспи...")
        exit()
    while number_try <= 2:
        number_try += 1
        e = random.randint(1, 10)
        print("Робот назвал число: ", e)
        if e < q:
            print("Твое число меньше того, что ПОЛЬЗОВАТЕЛЬ ЗАГАДАЛ")
        if e > q:
            print("Твое число больше того, что ПОЛЬЗОВАТЕЛЬ ЗАГАДАЛ")
        if q == e:
            break
    if q == e:
        print("УХ ТЫ, ТЫ УГАДАЛ, ПОЛЬЗОВАТЕЛЬ ЗАГАДАЛ: ", q, "Попыток потрачено: ", number_try)
    else:
        print("!!!GAME OVER!!!\nУХ ТЫ, ТЫ НЕ УГАДАЛ, ПОЛЬЗОВАТЕЛЬ ЗАГАДАЛ ЧИСЛО: ", q)

if zadanie == 3:
    print("\nЗадание:\n Продублируй число")


    def duplicate_largest_digit(n):
        largest = max(str(n))
        return int(str(n).replace(largest, largest * 2))


    a = int(input("Введите число: "))

    print(duplicate_largest_digit(a))

if zadanie == 4:
    print("\nЗадание:\n Числа Пифагора")


    def find_pythagorean(N):
        list = []
        count = 0
        for c in range(1, N):
            for b in range(1, c):
                for a in range(1, b):
                    if a * a + b * b == c * c:
                        list.append((a, b, c))
                        count += 1
                        if count == N:
                            return list
        return list


    a = int(input("Введите число: "))

    print(find_pythagorean(a))

if zadanie == 5:
    print("\nЗадание:\n Симулятор мармеладок")


    def sim_marmelad():
        taste = ["Кола", "Малиновый", "Вишневый", "Кислый лимон", "Киви"]
        form = ["Сердечки", "Мишки", "Цветы", "Змеи", "Кругляшки"]

        return print("Форма мармелада:", random.choice(form), "\nВкус мармелада:", random.choice(taste))


    sim_marmelad()

else:
    print("Самый умный нашелся? Иди поспи...")
