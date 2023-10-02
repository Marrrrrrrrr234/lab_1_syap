import random

# Первое задание
def first_task():

    # Функция для подсчёта суммы четных цифр у числа.
    def sum_odd_digits(number):
        even_counter = 0
        odd_sum = 0
        while number > 0:
            digit = number % 10
            if digit % 2 != 0:
                odd_sum += digit
            else:
                even_counter += 1
            number //= 10
        if even_counter == 0:
            return 0
        else:
            return odd_sum

    # Цикл для ввода числа, пока пользователь не выйдет
    while True:
        number = input("\nВведите натуральное число (При вводе '0' происходит выход из задания): ")
        if number == '0':
            break
        try:
            number = int(number)
            if number < 0:
                print("\tЭто отрицательное число!")
            else:
                print("\n Ответ:", sum_odd_digits(number))

        # Обработка неправильного ввода
        except ValueError:
            print("\nНеправильный ввод!")

# Второе задание
# Второе задание
def second_task():

    word = input("\nВведите слово: ")
    lower_pairs = 0
    upper_pairs = 0
    vowel_count = 0

    # Подсчет пар верхнего и нижнего регистра
    for i in range(len(word) - 1):
        if word[i].isupper() and word[i + 1].isupper():
            upper_pairs += 1
        elif word[i].islower() and word[i + 1].islower():
            lower_pairs += 1

    # Подсчет гласных букв
    for char in word:
        if char.lower() in "aeiouуёуеыаоэяию":
            vowel_count += 1

    print("\nКоличество пар нижнего регистра:", lower_pairs)
    print("\nКоличество пар верхнего регистра:", upper_pairs)
    print("\nКоличество гласных букв:", vowel_count)

# Третье задание
def third_task():

    # Метод для генерации рандомного списка
    def random_list(count, min_value, max_value):
        return [random.randint(min_value, max_value) for i in range(count)]

    numbers = random_list(10, -5, 5)

    print("\nВаш список:", numbers)

    # Идёт по числа на чётных позиция и считаем их произведение
    even_product = 1
    for i in range(len(numbers)):
        if i % 2 != 0:
            even_product *= numbers[i]

    list_length = len(numbers)

    print("\nПроизведение чисел с четными номерами:", even_product)

    print("\nДлина списка:", list_length)

# Четвертое задание
def fourth_task():

    first_word = input("\nВведите первое слово: ").lower()
    second_word = input("\nВведите второе слово: ").lower()

    # Если разная длина у слов, значит не анаграммы
    if len(first_word) != len(second_word):
        print("\nСлова не являются анаграммами.")

    else:
        # Преобразуем слова в списки символов
        first_word_list = list(first_word)
        second_word_list = list(second_word)

        reversed_second_word_list = second_word_list[::-1]

        # Сравниваем отсортированные списки
        if first_word_list == reversed_second_word_list:
            print("\nСлова являются анаграммами.")
        else:
            print("\nСлова не являются анаграммами.")

# Пятое задание
def fifth_task():

    # Метод для отображения описания
    def display_description(products):
        for product, details in products.items():
            print(f"{product} - {details[0]}")

    # Метод для отображения цены
    def display_price(products):
        for product, details in products.items():
            print(f"{product} - {details[1]}")

    # Метод для отображения количества
    def display_quantity(products):
        for product, details in products.items():
            print(f"{product} - {details[2]}")

    # Метод для отображения все информации
    def display_all_info(products):
        for product, details in products.items():
            print(f"{product} - {details[0]}, Цена: {details[1]}, Количество: {details[2]}")

    # Метод для совершения покупки
    def make_purchase(products):

        total_price = 0

        while True:
            product = input("\nВведите название изделия (Введите 'N', чтобы выйти): ")

            if product.lower() == 'n':
                break

            if product in products:
                try:
                    quantity = int(input("\nВведите количество желаемого товара: "))
                except ValueError:
                    print('Некорректное значение')

                if quantity <= 0:
                    print("\nНевозможно приобрести такое количество товара!")


                elif quantity <= products[product][2]:
                    products[product][2] -= quantity
                    total_price += products[product][1] * quantity

                else:
                    print("\nСлишком большая цена!")

            else:
                print("\nНет такого товара!")

        print("\nИтоговая цена:", total_price)

        print("\nОставшиеся товары:")

        display_quantity(products)

    # Список товаров в ювелирном магазине
    products = {
        "Кольцо": ["Отличное кольцо с бриллиантом!", 1000, 10],
        "Ожерелье": ["Невероятное ожерелье с рубином!", 3000, 10],
        "Серьги": ["Удивительные серьги с изумрудом!", 1500, 10],
        "Кулон": ["Отличный золотой кулон!", 2000, 10],
        "Бусы": ["Прекрасные бусы с аметистом!", 3500, 10]
    }

    while True:

        print("\n1. Отобразить описание"
              "\n2. Отобразить цену"
              "\n3. Отобразить количество"
              "\n4. Отобразить всю информацию"
              "\n5. Совершить покупку")

        choice = input("\nВведите название изделия (Введите 'N', чтобы выйти): ")

        if choice == '1':
            display_description(products)

        elif choice == '2':
            display_price(products)

        elif choice == '3':
            display_quantity(products)

        elif choice == '4':
            display_all_info(products)

        elif choice == '5':
            make_purchase(products)

        else:
            print("\nПока!")
            break

# Шестое задание
def sixth_task():

    # Метод для создания рандомного множества
    def random_set(count, min_value, max_value):
        return set(random.randint(min_value, max_value) for i in range(count))

    first_set = random_set(10, -10, 10)
    second_set = random_set(10, -10, 10)

    print("\nВаше первое множество:", first_set)
    print("\nВаш второе множество:", second_set)

    common_elements = first_set.intersection(second_set)

    if common_elements != 0:
        print("\nОдинаковые элементы в множествах:", common_elements)

    else:
        print("\nВ множествах нет повторяющихся элементов!")

# Основной метод программы
def menu():

    print("\nПривет пользователь!")

    while True:

        print("\nMenu:"
              "\n1. Первое задание"
              "\n2. Второе задание"
              "\n3. Третье задание"
              "\n4. Четвертое задание"
              "\n5. Пятое задание"
              "\n6. Шестое задание"
              "\nДругой ввод. Выход")

        choice = input("\nВведите номер задания: ")

        if choice == "1":
            first_task()

        elif choice == "2":
            second_task()

        elif choice == "3":
            third_task()

        elif choice == "4":
            fourth_task()

        elif choice == "5":
            fifth_task()

        elif choice == "6":
            sixth_task()

        else:
            print("\nПока!")
            break


if __name__ == "__main__":
    menu()


