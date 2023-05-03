from Flight import *
Y = Flight()
class Airport:
    def __init__(self):
        self.VA = []
        self.VAN = []
        self.ARR = []
        self.DEP = []
    def CheckAirport(self):
        self.k = len(self.VA)
        if self.k == 0:
            self.VAb = False
            print("FALSE")
        elif self.k > 0:
            for i in self.VA:
                if i == self.ICAO:
                    self.VAb = True
                    print("TRUE")
                    break
                elif i != self.ICAO:
                    self.VAb = False
                    print("FALSE")
        if self.VAb == False:
            self.VA=[self.ICAO,self.NAME]
            self.VAN.append(self.VA)
    def AddAirport(self):
        self.ICAO = str(input("ENTER YOUR NEW ICAO: "))
        self.NAME=str(input("INTRODUCE THE NAME OF THE ICAO: "))
        self.CheckAirport()
    def ListAirports(self):
        print(self.VAN)

    def GetArrivals(self):
        self.A = str(input("ENTER THE AIRPORT: "))
        self.ARR = []
        for i in range(len(Y.VF)):
            if Y.VFN[i] == self.A:
                self.ARR.append(Y.VF[i])
        print(self.ARR)
    def GetDepartures(self):
        self.D=str(input("ENTER THE AIRPORT: "))
        for n in Y.VF:
            for p in Y.VFN:
                if p == self.A:
                    self.DEP.append(Y.VFN)
        print(self.DEP)
    def PlotDepartures(self):
        import matplotlib.pyplot as plt
        x=str(input("ENTER THE AIRPORT: "))



