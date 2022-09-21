# 1 Рекурсия. Возведение числа x в степень y
# def power(x, y):
#         if (y == 1):
#                 return (x)
#         if (y != 1):
#                 return (x * power(x, y - 1))
#
#
# x=int(input('Введите х='))
# y=int(input('Введите у='))
# print( power(x, y))


# 2 Определить функцию, которая проверяет является ли строка, введенная пользователем, целым числом. Решение задачи сдать ссылкой на GitHub.
# def is_number(str):
#     try:
#         float(str)
#         return True
#     except ValueError:
#         return False
#
#
# a = input('Ведите число = ')
# print(is_number(a))


# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».


class IceCream:
    def __init__(self, ingredient):
         if isinstance(ingredient, str):
            self.ingredient = ingredient
         else:
            self.ingredient = None

    def my_icecream(self):
        if self.ingredient:
            print(f'Добавка {self.ingredient}')
        else:
            print('Без добавки')

icecream1 = IceCream('blyberry')
icecream1.my_icecream()



# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.

# class Car:
#     def __init__(self,maxprice=500):
#         self.__maxprice = maxprice
#
#     def set_price(self, maxprice):
#         self.__maxprice = maxprice
#
#     def get_price(self):
#         return self.__maxprice
#
# price = Car(120)
# print((price.get_price()))
# price.set_price(100)
# print(price.get_price())

# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')


class Animal:
    def  make_a_sound(self):
        print("Издает звук")


class Cat(Animal):
    def scratch():
        print()

    def make_a_sound(self):
        print("мяу")

class Dog(Animal):
    def make_a_sound(self):
        print("гав")



animal = Animal()
animal.make_a_sound()
cat = Cat()
cat.make_a_sound()
dog = Dog()
dog.make_a_sound()
