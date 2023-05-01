class Flight:
    def __init__(self):
        self.VF = []
        self.VFN = []
    def AddFlight(self):
        self.A = str(input("ENTER THE ARRIVAL AIRPORT: "))
        self.D = str(input("ENTER THE DEPARTURE AIRPORT: "))
        self.AT = str(input("ENTER THE TIME OF ARRIVAL: "))
        self.DT = str(input("ENTER THE TIME OF DEPARTURE: "))
        self.VF=[self.A,self.D,self.AT,self.DT]
        self.VFN.append(self.VF)
    def ListFlights(self):
        print(self.VFN)
