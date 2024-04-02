from dao.IVehicleService import IVehicleService
from entity.Vehicle import Vehicle
from dao.DatabaseContext import DatabaseContext
from exception.VehicleNotFoundException import VehicleNotFoundException

def get_connection():
    return DatabaseContext.getConnection(r'D:\Hexaware\CarConnect\util\db.properties')
class VehicleService(IVehicleService):
    def get_vehicle_by_id(self, vehicle_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE vehicleID = %s", (vehicle_id,))
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
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Vehicle WHERE availability = 1")
            vehicles_data = cursor.fetchall()

            if not vehicles_data:
                print("No Vehicles available!!")
                return None

            vehicles = []
            for vehicle_data in vehicles_data:
                vehicle = Vehicle(*vehicle_data)
                vehicles.append(str(vehicle))
            return vehicles

        except Exception as e:
            print("Error:", e)
            return None

    def add_vehicle(self, vehicle):

        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Vehicle (vehicleID, model, make, year, color,registrationNumber,availability,dailyRate) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                (vehicle.get_vehicleID(), vehicle.get_model(), vehicle.get_make(), vehicle.get_year(),
                 vehicle.get_color(), vehicle.get_registrationNumber(), vehicle.get_availability(),vehicle.get_dailyRate()))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_vehicle(self, vehicle):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Vehicle SET model=%s, make=%s, year=%s, color=%s,registrationNumber=%s,availability=%s,dailyRate=%s WHERE vehicleID=%s",
                (vehicle.get_model(), vehicle.get_make(), vehicle.get_year(), vehicle.get_color(),
                 vehicle.get_registrationNumber(),
                 vehicle.get_availability(), vehicle.get_dailyRate(), vehicle.get_vehicleID()))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def remove_vehicle(self, vehicle_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Vehicle WHERE vehicleID=%s", (vehicle_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

