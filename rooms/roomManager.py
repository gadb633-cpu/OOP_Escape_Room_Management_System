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
                    new_list_room = self.create_room_object(info_room)
                    DataManager("./db/rooms.json","./db/bookings.json").save_rooms(new_list_room)
                    print("Added successfully")
                case 4:
                    print(self.update_room())
                case 5:
                    room_id = f"R{UserInputs.get_num("enter room_id"):03d}"
                    for the_room in self.rooms:
                        if the_room.room_id == room_id:
                            status = self.update_is_active()
                            if status:
                                the_room.activate()
                            else:
                                the_room.deactivate()
                    DataManager("./db/rooms.json","./db/bookings.json").save_rooms(self.rooms)
                    print("Updated successfully!")
                case 6:
                    status_loop = False
                case _:
                    print("choice only between 1-6")

    def update_room(self):
        room_id = f"R{UserInputs.get_num("enter room id,(enter only num)"):03d}"
        info_to_update = self.choice_update_room()
        for room in self.rooms:
            if room.room_id == room_id:
                setattr(room, info_to_update[0], info_to_update[1])
                DataManager("./db/rooms.json","./db/bookings.json").save_rooms(self.rooms)
                return "Updated successfully!"
        return "not found!!"
    
    def choice_update_room(self):
        status_loop = True
        while status_loop:
            choice = UserInputs.get_str("enter your choice [name,difficulty,duration,min_players,max_players,price_per_player]")    
            match choice:
                case "name":
                    name = UserInputs.get_str("enter new name")
                    return [choice,name]
                case "difficulty":
                    difficulty = Validation.check_difficulty(UserInputs())
                    return [choice,difficulty]
                case "duration":
                    duration = UserInputs.get_num("enter new duration")
                    return [choice,duration]
                case "min_players":
                    min_players = UserInputs.get_num("enter new min_players")
                    return [choice,min_players]
                case "max_players":
                    max_players = UserInputs.get_num("enter new max_players")
                    return [choice,max_players]
                case "price_per_player":
                    price_per_player = UserInputs.get_num("enter new price_per_player")
                    return [choice,price_per_player]
                case _:
                    print("only in [name,difficulty,duration,min_players,max_players,price_per_player] !!!")

    def update_is_active(self):
        status_loop = True
        while status_loop:
            is_active = UserInputs.get_str("enter 1[true] or 0[false]")
            if is_active == "1":
                status_loop = False
                return True
            elif is_active =="0":
                status_loop = False
                return False
            print("only 1 or 0")

    def display_all_rooms(self):
        for room in self.rooms:
            room = room.to_dict()
            print("\n")
            for key,value in room.items():
                print(f"{key},{value}")

    def get_room(self,room_id):
        for room in self.rooms:
            room = room.to_dict()
            if room["room_id"] == room_id:
                return room
        raise ValueError(f"room {room_id} not found!")
    
    def get_info_room(self):
            name = UserInputs.get_str("enter name room")
            difficulty = Validation.check_difficulty(UserInputs())
            duration = UserInputs.get_num("enter duration")
            min_players = UserInputs.get_num("enter min_players")
            max_players = UserInputs.get_num("enter max_players")
            price_per_player = UserInputs.get_num("enter price_per_player")
            return [name,difficulty,duration,min_players,max_players,price_per_player]
    
    def create_room_object(self,info_room):
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