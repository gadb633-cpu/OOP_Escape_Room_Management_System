from data_manager.data_manager import DataManager
from helper.validation import Validation
from helper.inputs import UserInputs
from calculate_price.PricingManager import PricingManager

class EscapeRoomSystem:
    def __init__(self,data_manager,booking_manager,report_manager,rooms,bookings):
        self.data_manager =data_manager
        self.booking_manager = booking_manager
        self.report_manager = report_manager
        self.rooms=DataManager.load_rooms()
        self.bookings =DataManager.load_bookings()
        
    def add_order_id(orders):
        order_id = len(orders) + 1
        return f"B{order_id:03d}"
    
    def get_info_order(self):
        status_loop= True
        while status_loop:
            order_id = self.add_order_id(self.bookings)
            customer_name = UserInputs.get_str("enter your name")
            room_id = f"R{UserInputs.get_num("enter room_id"):03d}"
            Number_of_people = UserInputs.get_num("enter Number_of_people")
            room = Validation.val_info_order(self.rooms,room_id,Number_of_people)
            if room == False:
                continue
            while status_loop:
                booking_date = UserInputs.get_str("enter booking_date")
                day = PricingManager.find_day(booking_date)
                if Validation.check_format_input(booking_date,'%Y-%M-%d') == False:
                    continue
                if Validation.is_a_future_date(booking_date) == False:
                    continue
                start_time = UserInputs.get_str("enter start_time")
                if Validation.check_format_input(start_time,'%H:%M') == False:
                    continue
                list_time = PricingManager.convert_time(start_time)
                if Validation.is_between_the_range(list_time[0]+(list_time[1]/60)) == False:
                    continue
                if Validation.is_enough_time_before_closing(list_time[0]+(list_time[1]/60),room) == False:
                    continue
                if Validation.is_have_anther_order(self.bookings,room,room_id,booking_date,list_time) == False:
                    continue
                total_price = PricingManager.calculate_price(Number_of_people,room["price_per_player"],day)
                status_loop = False
        return [order_id,customer_name,room_id,booking_date,start_time,Number_of_people,total_price]  
      
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