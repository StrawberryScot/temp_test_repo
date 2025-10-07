class House():
    def __init__(self, number, door_color):
        self.floors = 2
        self.number = number
        self.door_color = door_color

    def get_details(self):
        return f"House number {self.number} has {self.floors} floors and a {self.door_color} door"

    def repaint_door(self, new_color):
        self.door_color = new_color
