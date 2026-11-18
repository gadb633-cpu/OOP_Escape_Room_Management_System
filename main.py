from data_manager.data_manager import DataManager
from helper.validation import Validation
from helper.inputs import UserInputs
from calculate_price.PricingManager import PricingManager
from booking.BookingManager import BookingManager
from Report.ReportManager import ReportManager

class EscapeRoomSystem:
    def __init__(self,data_manager,booking_manager,report_manager,rooms,bookings):
        self.data_manager =DataManager()
        self.booking_manager = BookingManager()
        self.report_manager = ReportManager()
        self.rooms=DataManager.load_rooms()
        self.bookings =DataManager.load_bookings()

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
    
    def choice_update(self,the_order,the_room,orders):
        status_loop = True
        while status_loop:
            choice = UserInputs.get_str("enter your choice [booking_date,start_time,players]")
            match choice:
                case "booking_date":
                    booking_date = UserInputs.get_str("enter new booking_date")
                    day = PricingManager.find_day(booking_date)
                    if Validation.check_format_input(booking_date,'%Y-%M-%d') == False:
                        continue
                    if Validation.is_a_future_date(booking_date) == False:
                        continue
                    total_price = PricingManager.calculate_price(the_order["players"],the_room["price_per_player"],day)
                    return [choice,booking_date,total_price]
                case "start_time":
                    start_time = UserInputs.get_str("enter start_time")
                    if Validation.check_format_input(start_time,'%H:%M') == False:
                        continue
                    list_time = PricingManager.convert_time(start_time)
                    if Validation.is_between_the_range(list_time[0]+(list_time[1]/60)) == False:
                        continue
                    if Validation.is_enough_time_before_closing(list_time[0]+(list_time[1]/60),the_room) == False:
                        continue
                    if Validation.is_have_anther_order(orders,the_room,the_order["room_id"],the_order["booking_date"],list_time) == False:
                        print("The time slot is not available!")
                        continue
                    return [choice,start_time,the_order["total_price"]]
                case "players":
                    players = UserInputs.get_num("enter players")
                    if Validation.check_num_people(the_room,players) == False:
                        continue
                    total_price = PricingManager.calculate_price(players,the_room["price_per_player"],PricingManager.find_day(the_order["booking_date"]))
                    return [choice,players,total_price]
                case _:
                    print("only in [booking_date,start_time,players] !!!")  
    
    def shaw_main_menu():
        print('''
        =========================================
            Escape Room Management System
        =========================================

        1. Rooms
        2. Orders
        3. Report
        4. Exit
        ''')
    def save_data(self):
        pass

    def run(self):
        pass   