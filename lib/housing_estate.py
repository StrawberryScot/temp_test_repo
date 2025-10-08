class HousingEstate:
    def __init__(self):
        self.houses = []

    def get_house_numbers(self):
        return [house.number for house in self.houses]
