class Drivers:
    def __init__(self,workId,name,startCity):
        self.workId=workId
        self.driver_name=driver_name
        self.startCity=startCity

class City:
    def __init__(self, name, neighbors):
        self.name = name
        self.neighbors = neighbors

class Best_Delivery:
    def __init__(self):
        self.drivers = []
        self.cities = {}
        self.driver_id_counter = 1