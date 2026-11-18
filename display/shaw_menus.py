
class Shaw_menus:
    @staticmethod
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
    @staticmethod
    def shaw_orders_menu():
        print('''
        =======================
                Orders
        =======================
        
            1. create new order
            2. Display all orders
            3. search order by id
            4. Display order by client
            5. Display order by date
            6. update order
            7. cancel order
            8. Exit
        ''')
    @staticmethod
    def shaw_rooms_menu():
        print('''
        =======================
                Rooms
        =======================

        1. Display all rooms
        2. Display room by id
        3. Add room
        4. update room
        5. Activating or Deactivating a Room
        6. Exit
        ''')     
            