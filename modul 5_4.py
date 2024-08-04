class Example:

    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        return object.__new__(cls)

    def __init__(self, first, second, third):
        print(first)
        print(second)
        print(third)

ex = Example('data', second=25, third=3.14)


class House:

    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    # def go_to(self, new_floor):
    #     self.new_floor = new_floor
    #     if new_floor < 1 or new_floor > self.number_of_floors:
    #         print('No such floor')
    #     for floor in range(new_floor):
    #         number = floor + 1
    #         if new_floor < self.number_of_floors:
    #             print(number)
    #
    # def __len__(self):
    #     return self.number_of_floors
    #
    # def __str__(self):
    #     return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'
    #
    # def __eq__(self, other):  # __eq__
    #     if isinstance(other, House):
    #         return self.number_of_floors == other.number_of_floors
    #
    # #  увеличивает кол-во этажей на переданное значение
    # #  value, возвращает сам объект self.
    # def __add__(self, value):
    #     self.number_of_floors += value
    #     return self
    #
    # def __iadd__(self, value):
    #     self.number_of_floors += value
    #     return self
    #
    # def __radd__(self, value):
    #     return self.__add__(value)
    #
    # def __gt__(self, other):  # __gt__
    #     if isinstance(other, House):
    #         return self.number_of_floors > other.number_of_floors
    #
    # def __ge__(self, other):  # __ge_
    #     if isinstance(other, House):
    #         return self.number_of_floors >= other.number_of_floors
    #
    # def __lt__(self, other):  # __lt__
    #     if isinstance(other, House):
    #         return self.number_of_floors < other.number_of_floors
    #
    # def __le__(self, other):  # __le__
    #     if isinstance(other, House):
    #         return self.number_of_floors <= other.number_of_floors
    #
    # def __ne__(self, other):  # __ne__
    #     if isinstance(other, House):
    #         return self.number_of_floors != other.number_of_floors


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
