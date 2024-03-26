from dao.IVehicleService import IVehicleService
from entity.Vehicle import Vehicle
from dao.DatabaseContext import DatabaseContext
from exception.VehicleNotFoundException import VehicleNotFoundException
class VehicleService(IVehicleService):
    def __init__(self, database_context):
        self.database_context = DatabaseContext

    def get_vehicle_by_id(self, vehicle_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = ?", (vehicle_id,))
            vehicle_data = cursor.fetchone()

            if not vehicle_data:
                raise VehicleNotFoundException("Vehicle with ID {} not found".format(vehicle_id))

            vehicle = Vehicle(*vehicle_data)
            return vehicle

        except Exception as e:
            print("Error:", e)
            return None

    def get_available_vehicles(self):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE availability = 1")
            vehicles_data = cursor.fetchall()

            if not vehicles_data:
                return "No Vehicles available!!"

            vehicles = []
            for vehicle_data in vehicles_data:
                vehicle = Vehicle(*vehicle_data)
                vehicles.append(vehicle)

            return vehicles

        except Exception as e:
            print("Error:", e)
            return None

    def add_vehicle(self, vehicle):

        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Vehicle (vehicleID, model, make, year, color,registrationNumber,availability,dailyRate) VALUES (?, ?, ?, ?, ?,?,?)",
                (Vehicle.vehicleID, Vehicle.model, Vehicle.make, Vehicle.year,
                 Vehicle.color, Vehicle.registrationNumber, Vehicle.availability,Vehicle.dailyRate))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_vehicle(self, vehicle):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Vehicle SET model=?, make=?, year=?, color=?,registrationNumber=?,availability=?,dailyRate=? WHERE vehicleID,=?",
                (Vehicle.vehicleID, Vehicle.model, Vehicle.make, Vehicle.year,
                 Vehicle.color, Vehicle.registrationNumber, Vehicle.availability, Vehicle.dailyRate))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def remove_vehicle(self, vehicle_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Vehicle WHERE vehicleID=?", (vehicle_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

