class House:
    def __init__(self,name:str,agency:str,addr:str,price:int,numBed:int,numBath:int) -> None:
        self.image = ""
        self.name = name
        self.agency = agency
        self.address = addr
        self.price = price
        self.description = ""
        self.numBedrooms = numBed
        self.numBathrooms = numBath
    
    def setImage(self,imageURL:str) -> None:
        self.image = imageURL
    
    def setDescription(self,desc:str) -> None:
        self.description = desc