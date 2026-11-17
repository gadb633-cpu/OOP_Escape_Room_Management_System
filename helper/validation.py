from datetime import datetime
from calculate_price.PricingManager import PricingManager

class Validation:
    @staticmethod
    def val_not_empty(name):
        if name =="":
            return False
        return True
    @staticmethod
    def is_positive(num):
        if num > 0:
            return True
        return False
    @staticmethod
    def is_name_exist(name,products):
        for product in products:
            if product["name"] ==name:
                return False
        return True
    @staticmethod    
    def check_is_category(search_by):
        if search_by in ["id","name","category","active","price"]:
            return True
        return False
    @staticmethod
    def check_format_input(start_time,format):
        try:
            time = datetime.strptime(start_time,format)
            return True
        except ValueError:
            print(f"only this format {format}")
            return False
    @staticmethod
    def is_have_anther_order(orders,room,room_id,booking_date,list_time:list):
        correct_min_new_order = (list_time[0]*60)+list_time[1]
        for order in orders:
            if order["room_id"] == room_id:
                if order["booking_date"] == booking_date:
                    if order["status"] =="Active":
                        time_order = PricingManager.convert_time(order["start_time"])
                        correct_min_order = (time_order[0]*60)+time_order[1]
                        start = (correct_min_order) - (room["duration"] +15)
                        end = (correct_min_order) + (room["duration"] +15)
                        if start < correct_min_new_order < end:
                            return False
        return True     
    @staticmethod
    def is_enough_time_before_closing(hour,room):
        if 22-(room["duration"]/60) >=hour:
            return True
        print("It is not possible to start a game at this time !!")
        return False
    @staticmethod
    def is_between_the_range(hour):
        if 10<=hour <=22:   
            return True
        return False
    @staticmethod
    def is_a_future_date(date):
        this_date = datetime.strptime(date,'%Y-%m-%d')
        now = datetime.today()
        if this_date < now:
            print("the date is in the past")
            return False
        return True
    @staticmethod
    def val_info_order(rooms,room_id,number_of_people):
        room = Validation.check_is_room_exist(rooms,room_id)
        if room == False:
            print("room id not found!")
            return False
        elif Validation.check_is_available(room) == False:
            print("the room not available !")
            return False
        elif Validation.check_num_people(room,number_of_people) == False:
            print("num of people not correct !")
            return False
        return room
    @staticmethod
    def check_is_available(room):
        if room["is_active"] ==True:
            return True
        return False
    @staticmethod
    def check_num_people(room,number_of_people):
        if room["min_players"] <= number_of_people:
            if number_of_people <= room["max_players"]:
                return True
        return False
    @staticmethod
    def check_is_room_exist(rooms,room_id):
        for room in rooms:
            if room["room_id"] == room_id:
                return room
        return  False