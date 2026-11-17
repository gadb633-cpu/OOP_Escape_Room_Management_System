from datetime import datetime

class PricingManager:
    def find_day(self,booking_date):
        time_date = datetime.strptime(booking_date,'%Y-%M-%d')
        return time_date.strftime("%A")
    
    def calculate_price(self,room, players, booking_date):
        if self.find_day(booking_date).lower() in ["friday","saturday"]:
            if 1 <= players <=4 :
                price = players*room["price_per_player"]
                return price + price*0.15
            elif 5<= players <=6:
                price = ((players*room["price_per_player"]) - ((players*room["price_per_player"])*0.10))
                return price + price*0.15
            elif players >=7:
                price = ((players*room["price_per_player"]) - ((players*room["price_per_player"])*0.15))
                return price + price*0.15
        else:
            if 1 <= players <=4 :
                return players*room["price_per_player"]
            elif 5<= players <=6:
                return (players*room["price_per_player"]) - ((players*room["price_per_player"])*0.10)
            elif players >=7:
                return (players*room["price_per_player"]) - ((players*room["price_per_player"])*0.15)
            
    def convert_time(self,start_time):
        time = datetime.strptime(start_time,"%H:%M")
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        return [hour,minute] 
        
    def convert_dates(self,date):
        convert_date = datetime.strptime(date,'%Y-%M-%d')
        day = int(convert_date.strftime("%d"))
        return day    
        
    def check_time_left(self,time_order:list):
        day_order = self.convert_dates(time_order[0])
        now = datetime.today()
        day_now = int(now.strftime("%d"))
        hour_now = now.strftime("%H:%M")
        list_time = self.convert_time(time_order[1])
        now_list_time = self.convert_time(hour_now)
        if day_now + 1 == day_order:
            if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) > 24*60:
                return 0
            if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) >= 6*60:
                return 25
            if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) < 6*60:
                return 50
        if day_now == day_order:
            if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) >= 6*60:
                return 25
            if (list_time[0]*60+list_time[1]) - (now_list_time[0]*60+now_list_time[1]) < 6*60:
                return 50
        return 0
        
    def calculate_cancellation_fee(self,booking,percent):
        if percent == 0:
            return 0
        elif percent == 25:
            return booking["total_price"] /4
        elif percent == 50:
            return booking["total_price"] /2