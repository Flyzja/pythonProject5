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


cucumber = House('ЖК Огурец', 25)
space = House('ЖК Космос', 75)
cucumber.go_to(48)
space.go_to(3)



