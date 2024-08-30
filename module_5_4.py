class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_floors):
        self.name = name
        self.number_of_floors = number_floors
    def go_to(self, new_floor):
        for f in range(new_floor + 1):
            if f <= self.number_of_floors and f >=  1:
                print(f)
            if new_floor > self.number_of_floors or self.number_of_floors < 1:
                    print('Такого этажа не существует')

                    return new_floor

    def __len__(self):
        return int(self.number_of_floors)

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        return (self.number_of_floors == other.number_of_floors)

    def __lt__(self, other):
        return (self.number_of_floors < other.number_of_floors)

    def __le__(self, other):
        return (self.number_of_floors <= other.number_of_floors)

    def __gt__(self, other):
        return (self.number_of_floors > other.number_of_floors)

    def __ge__(self, other):
        return (self.number_of_floors >= other.number_of_floors)

    def __ne__(self, other):
        return (self.number_of_floors != other.number_of_floors)

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(self.name, 'cнесён, но он останется в истории')

cucumber = House('ЖК Огурец', 25)
print(House.houses_history)
space = House('ЖК Космос', 75)
print(House.houses_history)

cucumber.go_to(48)
space.go_to(3)

# __str__
print(cucumber)
print(space)


# __len__
print(len(cucumber))
print(len(space))

#__eq__
print(cucumber == space)

#__lt__
print(cucumber < space)

#__le__
print(cucumber <= space)

#__gt__
print(cucumber > space)

#__ge__
print(cucumber >= space)

#__ne__
print(cucumber != space)

print(cucumber.__add__(7))
print(space.__add__(-7))

print(cucumber.__radd__(-7))
print(space.__radd__(7))

print(cucumber.__iadd__(3))
print(space.__iadd__(3))

birdhouse = House('ЖК Скворечник', 44)
print(House.houses_history)






