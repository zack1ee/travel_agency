class Flight:
    def __init__(self, airline, flight_no, takeoff, landing, cost):
        self.airline = airline
        self.flight_no = flight_no
        self.takeoff = takeoff
        self.landing = landing
        self.cost = cost
    
    def get_airline(self):
        return self.airline

    def get_flight_no(self):
        return self.flight_no
    
    def get_takeoff(self):
        return self.takeoff
    
    def get_landing(self):
        return self.landing
    
    def get_cost(self):
        return self.cost
    
    def to_string(self):
        return self.airline + " Flight " + str(self.flight_no) + " from " + self.takeoff + " to " + self.landing + " for $" + str(self.cost)