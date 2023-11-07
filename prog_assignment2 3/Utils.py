import random
from Flight import Flight
from Destination import Destination

class Utils:
    @staticmethod
    def add_flights_for_destination(destination, agency):
        country = destination.country
        airlines = ["American Airlines", "QANTAS", "JetStar", "Tiger Airways", "United Airlines", "Egypt Air", "Etihad", "Singapore Airlines", "British Air", "Cathay Dragon"]
        flight_min = 11
        flight_max = 999

        cost_min = 49.99
        cost_max = 999.99

        countries = []
        for d in agency.destinations.destinations:
            countries.append(d.country)
        
        for s in countries:
            try:
                agency.flights.add_flight(Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(flight_min, flight_max), country, s, round(random.uniform(cost_min, cost_max), 2)))
                agency.flights.add_flight(Flight(airlines[random.randint(0, (len(airlines) - 1))], random.randint(flight_min, flight_max), s, country, round(random.uniform(cost_min, cost_max), 2)))
            except:
                continue