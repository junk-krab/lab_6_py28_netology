# Домашнее задание к лекции 2.2 «Классы и их применение в Python»
# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#     гусей "Серый" и "Белый"
#     корову "Маньку"
#     овец "Барашек" и "Кудрявый"
#     кур "Ко-Ко" и "Кукареку"
#     коз "Рога" и "Копыта"
#     и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#     кормить
#     корову и коз доить
#     овец стричь
#     собирать яйца у кур, утки и гусей
#     различать по голосам(коровы мычат, утки крякают и т.д.)
# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.
# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#     Необходимо посчитать общий вес всех животных(экземпляров класса);
#     Вывести название самого тяжелого животного.
all_weight = []

class Animal(object):
    def __init__(self, name, weight, food, voice):
        self.name = name
        self.weight = weight
        self.food = food
        self.voice = voice
        all_weight.append(weight)

    def feed(self):
        return "Вы покормили %s и услышали довольное %s!" % (self.name, self.voice)

class Chicken(Animal):

    def collect(self):
        return "Вы собрали яйца у курицы с именем %s." % (self.name)

class Duck(Chicken):

    def collect(self):
        return "Вы собрали яйца у утки с именем %s." % (self.name)

class Goose(Chicken):

    def collect(self):
        return "Вы собрали яйца у гуся с именем %s." % (self.name)

class Cow(Animal):

    def milk(self):
        return "Корову с именем %s подоили!" % (self.name)

class Sheep(Animal):

    def shave(self):
        return "Козу %s остригли!" % (self.name)

class Goat(Cow):

    def milk(self):
        return "Корову с именем %s подоили!" % (self.name)

if __name__ == "__main__":

    first_chicken = Chicken("Ко-Ко", 5.5, "крошки", "Ко-Ко")
    print(first_chicken.collect())

    first_goat = Goat("Рога", 30.1, "трава", "Бе")
    print(first_goat.milk())

    first_duck = Duck("Кряква", 5.5, "крошки", "Кря")
    print(first_duck.collect())
    print(first_duck.voice)

    first_goose = Goose("Серый", 10.5, "крошки", "Га")
    print(first_goose.collect())
    print(first_goose.voice)

    first_cow = Cow("Манька", 350.0, "сено", "Мууу")
    print(first_cow.feed())
    print(first_cow.milk())
    print(first_cow.voice)

    first_sheep = Sheep("Барашек", 35.0, "сено", "Бее")
    print(first_sheep.shave())
    print(first_sheep.voice)

    second_sheep = Sheep("Кудрявый", 36.0, "сено", "Бее")
    print(second_sheep.shave())
    print(second_sheep.voice)

print("\nСумма всех животных", sum(all_weight))
print("\nМаксимальный вес животного:", max(all_weight))


