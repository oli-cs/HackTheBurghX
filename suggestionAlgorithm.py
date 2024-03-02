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
        ids = set(get_ids())#change this line when relevant method is done
        self.unseenIds = ids - self.get_seen_house_ids()
        return
    
    def get_house_to_display(self) -> dict:
        displayId = choice(self.unseenIds)#make this an actual algorithm at some point

        row = get_info(displayId)#change this line when relevant method is done
        return row

    def get_next_house(self):
        self.populate_unseen_houses_set()
        try:
            return self.get_house_to_display()
        except TypeError as e:
            print(str(e))
        return
    










    



    

    


