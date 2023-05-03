class Flight:
    def __init__(self):
        self.VF = []
        self.VFN = []
    def AddFlight(self):
        self.ARRIVALS = str(input("ENTER THE ARRIVAL AIRPORT: "))
        self.DEPARTURES = str(input("ENTER THE DEPARTURE AIRPORT: "))
        self.AT = int(input("ENTER THE TIME OF ARRIVAL: "))
        self.DT = int(input("ENTER THE TIME OF DEPARTURE: "))
        self.VFN=[self.ARRIVALS,self.DEPARTURES,self.AT,self.DT]
        self.VF.append(self.VFN)
    def ListFlights(self):
        print(self.VF)
