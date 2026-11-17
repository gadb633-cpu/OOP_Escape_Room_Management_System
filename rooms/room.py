
class Room:
    def __init__(self,room_id,name,difficulty,duration,min_players,max_players,price_per_player,is_active):
        self.room_id =room_id
        self.name =name 
        self.difficulty =difficulty 
        self.duration =duration 
        self.min_players  =min_players 
        self.max_players =max_players 
        self.price_per_player =price_per_player 
        self.is_active =is_active 

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False  

    def is_valid_players(self,players):
        if self.min_players <= players:
            if players <= self.max_players:
                return True
        return False

    def to_dict(self):
        return {
        "room_id": self.room_id,
        "name": self.name,
        "difficulty": self.difficulty,
        "duration": self.duration,
        "min_players": self.min_players,
        "max_players": self.max_players,
        "price_per_player": self.price_per_player,
        "is_active": self.is_active}
    
    @classmethod
    def from_dict(cls,room:dict):
        return cls(room.get("room_id"),room.get("name"),room.get("difficulty"),room.get("duration"),room.get("min_players"),room.get("max_players"),room.get("price_per_player"),room.get("is_active"))
    
    
room1 = Room(1,"gad","easy",60,1,1,1,True)   
print(room1.to_dict())
print(room1.from_dict(room1.to_dict())) 