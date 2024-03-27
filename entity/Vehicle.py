class Vehicle:
    def __init__(self, vehicleID, model, make, year, color, registrationNumber, availability, dailyRate):
        self.__vehicleID = vehicleID
        self.__model = model
        self.__make = make
        self.__year = year
        self.__color = color
        self.__registrationNumber = registrationNumber
        self.__availability = availability
        self.__dailyRate = dailyRate

    def get_vehicleID(self):
        return self.__vehicleID

    def set_vehicleID(self, value):
        self.__vehicleID = value

    def get_model(self):
        return self.__model

    def set_model(self, value):
        self.__model = value

    def get_make(self):
        return self.__make

    def set_make(self, value):
        self.__make = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        self.__year = value

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value

    def get_registrationNumber(self):
        return self.__registrationNumber

    def set_registrationNumber(self, value):
        self.__registrationNumber = value

    def get_availability(self):
        return self.__availability

    def set_availability(self, value):
        self.__availability = value

    def get_dailyRate(self):
        return self.__dailyRate

    def set_dailyRate(self, value):
        self.__dailyRate = value

    def print_info(self):
        print("Vehicle ID:", self.__vehicleID)
        print("Model:", self.__model)
        print("Make:", self.__make)
        print("Year:", self.__year)
        print("Color:", self.__color)
        print("Registration Number:", self.__registrationNumber)
        print("Availability:", self.__availability)
        print("Daily Rate:", self.__dailyRate)

    def __str__(self):
        return (f"Vehicle ID: {self.__vehicleID}, Model: {self.__model}, Make: {self.__make}, "
                f"Year: {self.__year}, Color: {self.__color}, Registration Number: {self.__registrationNumber}, "
                f"Availability: {self.__availability}, Daily Rate: {self.__dailyRate}")