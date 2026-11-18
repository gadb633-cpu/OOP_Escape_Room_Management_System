from data_manager.data_manager import DataManager
from display.shaw_menus import Shaw_menus
from helper.inputs import UserInputs
from helper.validation import Validation
from rooms.room import Room
class RoomManager:
    def __init__(self):
        self.rooms =DataManager("./db/rooms.json","./db/bookings.json").load_rooms()

    def Room_Management(self):
        status_loop = True
        while status_loop:
            Shaw_menus.shaw_rooms_menu()
            choice = UserInputs.get_num("enter your choice")
            match choice:
                case 1:
                    self.display_all_rooms()
                case 2:
                    room_id = f"R{UserInputs.get_num("enter room_id"):03d}"
                    print(self.get_room(room_id))
                case 3:
                    info_room = self.get_info_room()
                    new_list_room = self.create_room(info_room)
                    DataManager("./db/rooms.json","./db/bookings.json").save_rooms(new_list_room)
                    print("Added successfully")
                case 4:
                    pass
                    # print(update_room("./db/rooms.json"))
                case 5:
                    pass
                    # print(update_is_active("./db/rooms.json"))
                case 6:
                    status_loop = False
                case _:
                    print("choice only between 1-6")

    def display_all_rooms(self):
        for room in self.rooms:
            room = room.to_dict()
            print("\n")
            for key,value in room.items():
                print(f"{key},{value}")

    def get_room(self,room_id):
        for room in self.rooms:
            if room.to_dict()["room_id"] == room_id:
                return room.to_dict()
        raise ValueError(f"room {room_id} not found!")
    
    def get_info_room(self):
            name = UserInputs.get_str("enter name room")
            difficulty = Validation.check_difficulty(UserInputs())
            duration = UserInputs.get_num("enter duration")
            min_players = UserInputs.get_num("enter min_players")
            max_players = UserInputs.get_num("enter max_players")
            price_per_player = UserInputs.get_num("enter price_per_player")
            return [name,difficulty,duration,min_players,max_players,price_per_player]
    
    def create_room(self,info_room):
        new_room= {
            "room_id": f"R{len(self.rooms)+1:03d}",
            "name": info_room[0],
            "difficulty": info_room[1],
            "duration": info_room[2],
            "min_players": info_room[3],
            "max_players": info_room[4],
            "price_per_player": info_room[5],
            "is_active": True
            }
        new_room_object = Room.from_dict(new_room)
        objects = self.rooms
        objects.append(new_room_object)
        return objects
    