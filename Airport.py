class Airport:
    def __init__(self):
        self.VA = []
        self.VAN = []
    def CheckAirport(self):
        self.k = len(self.VAN)
        if self.k == 0:
            self.VAb = False
            print("FALSE")
        elif self.k > 0:
            for i in self.VAN:
                if i == self.ICAO:
                    self.VAb = True
                    print("TRUE")
                    break
                elif i != self.ICAO:
                    self.VAb = False
                    print("FALSE")
        if self.VAb == False:
            self.VAN.append(self.ICAO)
            self.VAN.append(self.NAME)
            self.VA.append(self.VAN)
    def AddAirport(self):
        self.ICAO = str(input("ENTER YOUR NEW ICAO: "))
        self.NAME=str(input("INTRODUCE THE NAME OF THE ICAO: "))
        self.CheckAirport()
    def ListAirports(self):
        print(self.VA)

    def GetArrivals(A, VF):
        arrivals = []
        for flight in VF:
            if flight.arrival == A.ICAO:
                arrivals.append(flight)
        return arrivals

    def GetDepartures(A, VF):
        departures = []
        for flight in VF:
            if flight.departure == A.ICAO:
                departures.append(flight)
        return departures

    def PlotDepartures(VA, VF):
        import matplotlib.pyplot as plt

        airport_departures = {}

        for airport in VA:
            departures = VA.GetDepartures(airport, VF)
            airport_departures[airport.ICAO] = len(departures)

        plt.bar(airport_departures.keys(), airport_departures.values())
        plt.xlabel("Airport ICAO")
        plt.ylabel("Number of Departures")
        plt.title("Departures per Airport")
        plt.show()


