from random import choice
from database import *
from statistics import stdev
class HouseTinder():
    def __init__(self):
        self.rightHouseIds = set()
        self.leftHouseIds = set()
        self.unseenIds = set()
        self.rightPrices = []
        self.rightNumBeds = []
        self.rightNumBaths = []
        self.priceStdDev = 0
        self.numBedsStdDev = 0
        self.numBathsStdDev = 0

    def get_seen_house_ids(self) -> set:
        return self.rightHouseIds.union(self.leftHouseIds)
    
    def append_right(self,id:int) -> None:
        self.rightHouseIds.add(id)
        connect_db()
        data = get_info(id)
        close_db()
        self.rightPrices.append(data[4])
        self.rightNumBeds.append(data[2])
        self.rightNumBaths.append(data[3])
        if len(self.rightHouseIds) > 1:
            self.priceStdDev = stdev(self.rightPrices)
            self.numBedsStdDev = stdev(self.rightNumBeds)
            self.numBathsStdDev = stdev(self.rightNumBaths)
        return

    def append_left(self,id:int) -> None:
        self.leftHouseIds.add(id)
        return
    
    def populate_unseen_houses_set(self) -> None:
        connect_db()
        ids = set(get_ids())
        close_db()
        self.unseenIds = ids - self.get_seen_house_ids()#unseen ids = all ids set minus seen ids
        return
    
    def choose_house(self,idArray:list) -> int:
        return choice(idArray)

    def get_house_to_display(self) -> list:
        displayId = self.choose_house(list(self.unseenIds))#make this an actual algorithm at some point
        connect_db()
        row = get_info(displayId)#change this line when relevant method is done
        close_db()
        return row

    def get_next_house(self) -> list:
        self.populate_unseen_houses_set()
        if len(self.unseenIds) == 0:
            return []
        return self.get_house_to_display()
    










    



    

    


