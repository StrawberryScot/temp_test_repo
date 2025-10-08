from lib.housing_estate import HousingEstate
from lib.house import House

def test_add_houses_to_housing_estate():
    house1 = House(137, "white")
    house2 = House(24, "red")
    housing_estate = HousingEstate()
    housing_estate.houses.append(house1)
    housing_estate.houses.append(house2)
    assert housing_estate.houses == [house1, house2]

def test_get_house_from_housing_estate():
    house1 = House(137, "white")
    house2 = House(24, "red")
    housing_estate = HousingEstate()
    housing_estate.houses.append(house1)
    housing_estate.houses.append(house2)
    assert housing_estate.get_house_numbers() == [137, 24]
