from data_manager.data_manager import DataManager
from calculate_price.PricingManager import PricingManager
from helper.validation import Validation
from rooms.roomManager import RoomManager
from display.shaw_menus import Shaw_menus
from helper.inputs import UserInputs
from booking.Booking import Booking
class BookingManager:
    def __init__(self):
        self.rooms =DataManager("./db/rooms.json","./db/bookings.json").load_rooms()
        self.bookings =DataManager("./db/rooms.json","./db/bookings.json").load_bookings()
        self.pricing_manager = PricingManager()

    def booking_management(self):
        status_loop = True
        while status_loop:
            Shaw_menus.shaw_orders_menu()
            choice = UserInputs.get_num("enter your choice")
            match choice:
                case 1:
                    status =True
                    while status:
                        try:
                            info_to_create = self.get_info_order()
                            print(self.create_booking(info_to_create[0],info_to_create[1],info_to_create[2],info_to_create[3],info_to_create[4]))
                            status = False
                        except ValueError as error:
                            print(f"error {error}")
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    status_loop = False    
                case _:
                    print("choice only between 1-8")

    def get_booking_id(self):
        return f"B{len(self.bookings) + 1:03d}"
    
    def get_info_order(self):
        status_loop= True
        while status_loop:
            customer_name = UserInputs.get_str("enter your name")
            room_id = f"R{UserInputs.get_num("enter room_id"):03d}"
            players = UserInputs.get_num("enter Number_of_people")
            booking_date = UserInputs.get_str("enter booking_date")
            start_time = UserInputs.get_str("enter start_time")
            status_loop = False
        return [customer_name,room_id,booking_date,start_time,players] 
    
    def create_booking(self,customer_name, room_id, booking_date, start_time, players):
        room = RoomManager().get_room(room_id)
        if not Validation.check_is_available(room):
            raise ValueError(f"room {room_id} not available!")
        if not Validation.check_num_people(room,players):
            raise ValueError(f"num {players} not correct!")
        if not Validation.check_format_input(booking_date,'%Y-%m-%d') or not Validation.is_a_future_date(booking_date):
            raise ValueError
        if not Validation.check_format_input(start_time,'%H:%M'):
            raise ValueError
        list_time = PricingManager().convert_time(start_time)
        if not Validation.is_between_the_range(list_time[0]+(list_time[1]/60)):
            raise ValueError("it's out of time!")
        if not Validation.is_enough_time_before_closing(list_time[0]+(list_time[1]/60),room):
            raise ValueError("It is not possible to start a game at this time !!")
        if not Validation.is_have_anther_order(self.bookings,room,room_id,booking_date,list_time):
            raise ValueError("already booking at this time exist! ")

        new_booking =  {
        "booking_id": self.get_booking_id(),
        "customer_name": customer_name,
        "room_id": room_id,
        "booking_date": booking_date,
        "start_time": start_time,
        "players": players,
        "total_price": PricingManager().calculate_price(room,players,booking_date),
        "status": "Active",
        "cancellation_fee": 0.0}

        new_booking_object = Booking.from_dict(new_booking)
        self.bookings.append(new_booking_object)
        DataManager("./db/rooms.json","./db/bookings.json").save_bookings(self.bookings)
        return "added successfully"
    
          
    def get_booking(self, booking_id: str):
        for booking in self.bookings:
            if booking.to_dict()["booking_id"] == booking_id:
                return booking.to_dict()
        raise ValueError(f"order {booking_id} not found!")
    
    def get_customer_bookings(self,customer_name):
        for booking in self.bookings:
            if booking.to_dict()["customer_name"] ==customer_name:
                return booking 

    def get_bookings_by_date(self,booking_date):
        for booking in self.bookings:
            if booking.to_dict()["booking_date"] ==booking_date:
                return booking
            
    def check_availability(self,room_id, booking_date, start_time, exclude_booking_id=None):
        pass

    def update_booking(self,booking_id, booking_date, start_time, players):
        pass

    def cancel_booking(self,booking_id, current_datetime):
        pass
    