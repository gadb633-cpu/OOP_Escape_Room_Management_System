from helper.validation import Validation

class UserInputs:
    @staticmethod
    def get_num(msg):
        status_loop = True
        while status_loop:
            try:
                num = int(input(f"{msg}:").strip())
                if Validation.is_positive(num) == False:
                    print("enter positive num")
                    continue
                status_loop = False
                return num
            except ValueError as error:
                print(f"{error},try again!!")
    @staticmethod            
    def get_str(msg):
        status_loop = True
        while status_loop:
            name = input(f"{msg}:").strip()
            if Validation.val_not_empty(name) == False:
                continue
            status_loop = False
            return name         
