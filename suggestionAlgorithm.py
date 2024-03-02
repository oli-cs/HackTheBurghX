from random import choice
from database import *
class houseTinder():
    def __init__(self):
        self.rightHouseIds = set()

        self.leftHouseIds = set()
        self.unseenIds = set()

    def getSeenHouseIds(self) -> set:
        return self.rightHouseIds.union(self.leftHouseIds)
    
    def appendRight(self,id:int) -> None:
        self.rightHouseIds.add(id)
        return

    def appendLeft(self,id:int) -> None:
        self.leftHouseIds.add(id)
        return
    
    def populateUnseenHousesSet(self) -> None:
        ids = set(getIds())#change this line when relevant method is done
        self.unseenIds = ids - self.getSeenHouseIds()
        return
    
    def getHouseToDisplay(self) -> dict:
        displayId = choice(self.unseenIds)#make this an actual algorithm at some point

        row = getInfoForId(displayId)#change this line when relevant method is done
        if type(row) == dict:
            return row
        raise TypeError("type of `row` is {rowType} not dict".format(type(row)))

    def getNexthouse(self):
        self.populateUnseenHousesSet()
        try:
            return self.getHouseToDisplay()
        except TypeError as e:
            print(str(e))
        return
    










    



    

    


