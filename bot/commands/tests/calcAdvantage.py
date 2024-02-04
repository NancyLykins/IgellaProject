def calcAdvantage(attr):
    
    modFor = attr%2
    floorAttr = 0
    if(modFor):
        floorAttr = (attr - 11)    
    
    else:
        floorAttr = attr - 10 

    return int((floorAttr)/2)