from data_manager.data_manager import DataManager
from calculate_price.PricingManager import PricingManager
from rooms.room import Room
from booking.Booking import Booking
from helper.inputs import UserInputs

class BookingManager:
    def __init__(self):
        self.rooms =[Room.from_dict(room) for room in DataManager.load_rooms()]
        self.bookings =[Booking.from_dict(booking) for booking in DataManager.load_bookings()]
        self.pricing_manager = PricingManager()
    
    def create_booking(self,customer_name, room_id, booking_date, start_time, players,total_price):
        new_booking = Booking.to_dict(len(self.bookings)+1,customer_name,room_id,booking_date,start_time,players,total_price,status=True,cancellation_fee=0.0)
        new_booking_object= Booking.from_dict(new_booking)
        self.bookings.append(new_booking_object)

    def get_booking(self,booking_id):
        pass

    def get_customer_bookings(self,customer_name):
        pass

    def get_bookings_by_date(self,booking_date):
        pass

    def check_availability(self,room_id, booking_date, start_time, exclude_booking_id=None):
        pass

    def update_booking(self,booking_id, booking_date, start_time, players):
        pass

    def cancel_booking(self,booking_id, current_datetime):
        pass
    