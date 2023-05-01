from Airport import *
from Flight import *
a = True
z = Airport()
y = Flight()
while a:
    print("--------------------MENU------------------------")
    print("1. NEW FLIGHT")
    print("2. NEW AIRPORT")
    print("3. SHOW THE LIST OF AIRPORTS AND FLIGHTS")
    print("4. SHOW ALL ARRIVALS OF AN AIRPORT")
    print("5. PLOT DEPARTURES")
    print("6. END PROGRAM")
    print("------------------------------------------------")
    x = str(input("SELECT AN OPTION: "))

    if x == "1":
        y.AddFlight()
    elif x == "2":
        z.AddAirport()
    elif x == "3":
        print("THE LIST OF AIRPORTS IS:")
        z.ListAirports()
        print("THE LIST OF FLIGHTS IS:")
        y.ListFlights()
    elif x == "4":
        z.GetArrivals()
    elif x == "5":
        z.PlotDepartures()
    elif x == "6":
        a = False
    else:
        print("Error")