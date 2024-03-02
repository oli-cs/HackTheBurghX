from random import choice
from database import *
class HouseTinder():
    def __init__(self):
        self.rightHouseIds = set()

        self.leftHouseIds = set()
        self.unseenIds = set()

    def get_seen_house_ids(self) -> set:
        return self.rightHouseIds.union(self.leftHouseIds)
    
    def append_right(self,id:int) -> None:
        self.rightHouseIds.add(id)
        return

    def append_left(self,id:int) -> None:
        self.leftHouseIds.add(id)
        return
    
    def populate_unseen_houses_set(self) -> None:
        connect_db()
        ids = set(get_ids())
        close_db()
        self.unseenIds = ids - self.get_seen_house_ids()
        return
    
    def get_house_to_display(self) -> dict:
        displayId = 2#choice(list(self.unseenIds))#make this an actual algorithm at some point
        connect_db()
        row = get_info(displayId)#change this line when relevant method is done
        close_db()
        return row

    def get_next_house(self) -> list:
        self.populate_unseen_houses_set()
        return self.get_house_to_display()
    










    



    

    


