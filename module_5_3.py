class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def go_to(self, new_floor):
        if new_floor > self.floor:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floor}"

    def __eq__(self, other):
        return self.floor == other.floor

    def __lt__(self, other):
        return self.floor < other.floor

    def __gt__(self, other):
        return self.floor > other.floor

    def __ge__(self, other):
        return self.floor >= other.floor

    def __le__(self, other):
        return self.floor <= other.floor

    def __ne__(self, other):
        return self.floor != other.floor

    def __iadd__(self, value):
        self.floor += value
        return self

    def __add__(self, value):
        return House(self.name, self.floor + value)

    def __radd__(self, value):
        return House(self.name, self.floor + value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)
print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

