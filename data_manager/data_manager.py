import json

class DataManager:
    def __init__(self,rooms_file ,bookings_file ):
        self.rooms_file =rooms_file 
        self.bookings_file =bookings_file 

    def load_rooms(self):
        try:
            with open(self.rooms_file,"r", encoding="utf-8") as file:
                room_data = file.read()
                room_data = json.loads(room_data)
            return room_data
        except FileNotFoundError:
            return []

    def load_bookings(self):
        try:
            with open(self.bookings_file,"r", encoding="utf-8") as file:
                booking_data = file.read()
                booking_data = json.loads(booking_data)
            return booking_data
        except FileNotFoundError:
            return [] 

    def save_rooms(self,rooms):
        with open(self.rooms_file, "w") as file:
            data = json.dumps(rooms,indent=4)
            file.write(data)

    def save_bookings(self,bookings):
        with open(self.bookings_file, "w") as file:
            data = json.dumps(bookings,indent=4)
            file.write(data)