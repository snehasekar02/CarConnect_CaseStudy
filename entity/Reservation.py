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

    @property
    def reservationID(self):
        return self.__reservationID

    @reservationID.setter
    def reservationID(self, value):
        self.__reservationID = value

    @property
    def customerID(self):
        return self.__customerID

    @customerID.setter
    def customerID(self, value):
        self.__customerID = value

    @property
    def vehicleID(self):
        return self.__customerID

    @vehicleID.setter
    def vehicleID(self, value):
        self.__vehicleID = value

    @property
    def startDate(self):
        return self.__startDate

    @startDate.setter
    def startDate(self, value):
        self.__startDate = value

    @property
    def endDate(self):
        return self.__endDate

    @endDate.setter
    def endDate(self, value):
        self.__endDate = value

    @property
    def totalCost(self):
        return self.__totalCost

    @totalCost.setter
    def totalCost(self, value):
        self.__totalCost = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def calculateTotalCost(self):
        """This method is called when the customer needs an insurance policy"""
        duration_in_days = (self.endDate - self.startDate).days
        rate_per_day = Vehicle.dailyRate
        insurance_per_day = 20
        insurance = insurance_per_day * duration_in_days
        total_cost = (duration_in_days * rate_per_day) + insurance
        self.totalCost = total_cost
