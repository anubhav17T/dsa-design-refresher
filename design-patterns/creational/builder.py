# Product
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None
        self.windows = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.doors} doors, {self.windows} windows"

# Builder
class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, count):
        self.house.walls = count
        return self

    def build_roof(self, type_):
        self.house.roof = type_
        return self

    def build_doors(self, count):
        self.house.doors = count
        return self

    def build_windows(self, count):
        self.house.windows = count
        return self

    def build(self):
        return self.house

# Client
builder = HouseBuilder()
villa = builder.build_walls(4).build_roof("Gable").build_doors(2).build_windows(6).build()
print(villa)

cottage = builder.build_walls(2).build_roof("Flat").build_doors(1).build_windows(4).build()
print(cottage)