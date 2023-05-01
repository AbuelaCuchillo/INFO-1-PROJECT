class Airport:
    def __init__(self):
        self.VA = []
        self.VAN = []
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

    