class Animal:
    alive = True
    fed = False
    name = None

    def __init__(self, name):
        self.name = name


class Plant:
    edible = False
    name = None

    def __init__(self, name):
        self.name = name


class Predator(Animal):
    food = None

    def eat(self, food):
        self.food = food
        if food:
            print(f'{self.name} съел {food.name}')
        elif not food:
            print(f'{self.name} не стал есть {food.name}')


class Mammal(Animal):
    food = None

    def eat(self, food):
        if food:
            print(f'{self.name} съел {food.name}')
        elif not food:
            print(f'{self.name} не стал есть {food.name}')


class Flower(Plant):
    food = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уол-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
