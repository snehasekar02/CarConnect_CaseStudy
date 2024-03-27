from entity.Vehicle import Vehicle


class Reservation:
    def __init__(self, reservationID, customerID, vehicleID, startDate, endDate, totalCost, status):
        self.__reservationID = reservationID
        self.__customerID = customerID
        self.__vehicleID = vehicleID
        self.__startDate = startDate
        self.__endDate = endDate
        self.__totalCost = totalCost
        self.__status = status

    def get_reservationID(self):
        return self.__reservationID

    def set_reservationID(self, value):
        self.__reservationID = value

    def get_customerID(self):
        return self.__customerID

    def set_customerID(self, value):
        self.__customerID = value

    def get_vehicleID(self):
        return self.__vehicleID

    def set_vehicleID(self, value):
        self.__vehicleID = value

    def get_startDate(self):
        return self.__startDate

    def set_startDate(self, value):
        self.__startDate = value

    def get_endDate(self):
        return self.__endDate

    def set_endDate(self, value):
        self.__endDate = value

    def get_totalCost(self):
        return self.__totalCost

    def set_totalCost(self, value):
        self.__totalCost = value

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    def calculateTotalCost(self):
        """This method is called when the customer needs an insurance policy"""
        duration_in_days = (self.__endDate - self.__startDate).days
        rate_per_day = Vehicle.dailyRate
        insurance_per_day = 20
        insurance = insurance_per_day * duration_in_days
        total_cost = (duration_in_days * rate_per_day) + insurance
        self.__totalCost = total_cost

    def print_info(self):
        print("Reservation ID:", self.__reservationID)
        print("Customer ID:", self.__customerID)
        print("Vehicle ID:", self.__vehicleID)
        print("Start Date:", self.__startDate)
        print("End Date:", self.__endDate)
        print("Total Cost:", self.__totalCost)
        print("Status:", self.__status)
