class houseTinderAlgo():
    def __init__(self):
        self.rightHouseIds = set()
        self.leftHouseIds = set()

    def getSeenHouseIds(self) -> set:
        return self.rightHouseIds.union(self.leftHouseIds)
    
    def appendRight(self,id:int) -> None:
        self.rightHouseIds.add(id)
        return

    def appendLeft(self,id:int) -> None:
        self.leftHouseIds.add(id)
        return
    
    def getNextHouse(self) -> dict:
        pass

    


