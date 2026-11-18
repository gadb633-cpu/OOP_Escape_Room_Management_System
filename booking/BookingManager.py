from data_manager.data_manager import DataManager
from calculate_price.PricingManager import PricingManager
from helper.validation import Validation
from rooms.roomManager import RoomManager

class BookingManager:
    def __init__(self):
        self.rooms =DataManager("./db/rooms.json","./db/bookings.json").load_rooms()
        self.bookings =DataManager("./db/rooms.json","./db/bookings.json").load_bookings()
        self.pricing_manager = PricingManager()

    def get_booking_id(self):
        booking_id = len(self.bookings) + 1
        return f"B{booking_id:03d}"
     
    def create_booking(self,customer_name, room_id, booking_date, start_time, players):
        room = RoomManager.get_room(room_id)
        if not Validation.check_is_available(room):
            raise ValueError(f"room {room_id} not available!")
        if not Validation.check_num_people(room,players):
            raise ValueError(f"num {players} not correct!")
        if not Validation.check_format_input(booking_date,'%Y-%m-%d') or not Validation.is_a_future_date(booking_date):
            raise ValueError
        if not Validation.check_format_input(start_time,'%H:%M'):
            raise ValueError
        list_time = PricingManager.convert_time(start_time)
        if not Validation.is_between_the_range(list_time[0]+(list_time[1]/60)):
            raise ValueError("it's out of time!")
        if not Validation.is_enough_time_before_closing(list_time[0]+(list_time[1]/60),room):
            raise ValueError("It is not possible to start a game at this time !!")
        if not Validation.is_have_anther_order(self.bookings,room,room_id,booking_date,list_time):
            raise ValueError("already booking at this time exist! ")

        return {
        "booking_id": self.get_booking_id(),
        "customer_name": customer_name,
        "room_id": room_id,
        "booking_date": booking_date,
        "start_time": start_time,
        "players": players,
        "total_price": PricingManager.calculate_price(room,players,booking_date),
        "status": "Active",
        "cancellation_fee": 0.0}
        
        
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
    