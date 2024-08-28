class House:
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

cucumber = House('ЖК Огурец', 25)
space = House('ЖК Космос', 75)
cucumber.go_to(48)
space.go_to(3)

# __str__
print(cucumber)
print(space)

# __len__
print(len(cucumber))
print(len(space))
