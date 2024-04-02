from dao.VehicleService import VehicleService
from dao.CustomerService import CustomerService
from dao.ReservationService import ReservationService
from dao.AdminService import AdminService
from dao.DatabaseContext import DatabaseContext


def get_connection():
    return DatabaseContext.getConnection(r'D:\Hexaware\CarConnect\util\db.properties')


class ReportGenerator:
    @staticmethod
    def generate_vehicle_report(vehicleID):
        v = VehicleService()
        vehicle = v.get_vehicle_by_id(vehicleID)
        if vehicle:
            print(f"ID: {vehicle.get_vehicleID()}")
            print(f"Registration ID: {vehicle.get_registrationNumber()}")
            print(f"Vehicle model : {vehicle.get_model()}")
            print(f"Vehicle color: {vehicle.get_color()}")
            print(f"Vehicle dailyrate: {vehicle.get_dailyRate()}")
            print(f"Vehicle availability: {vehicle.get_availability()}")
        else:
            print("Vehicle not found.")

    @staticmethod
    def generate_customer_report(Customer_ID):
        c = CustomerService()
        customer = c.get_customer_by_id(Customer_ID)
        if customer:
            print(f"\nCustomer ID {customer.get_customer_id()}")
            print(f"Name: {customer.get_first_name() + customer.get_last_name()}")
            print(f"Username: {customer.get_username()}")
            print(f"Email: {customer.get_email()}")
            print(f"Phone_number: {customer.get_phone_number()}")
            print(f"Address: {customer.get_address()}")
        else:
            print("Customer not found.")

    @staticmethod
    def generate_reservation_report(Reservation_ID):
        r = ReservationService()
        reservation = r.get_reservation_by_id(Reservation_ID)
        if reservation:
            print(f"\nReservation ID: {reservation.get_reservationID()}")
            print(f"Customer ID: {reservation.get_customerID()}")
            print(f"Vehicle ID: {reservation.get_customerID()}")
            print(f"Status: {reservation.get_status()}")
            print(f"Cost: {reservation.get_totalCost()}")
        else:
            print("Reservation not found.")

    @staticmethod
    def generate_admin_report(Admin_ID):
        a = AdminService()
        admin = a.get_admin_by_id(Admin_ID)
        if admin:
            print(f"\nAdmin id: {admin.get_adminID()}")
            print(f"Admin name: {admin.get_firstName() + admin.get_lastName()}")
            print(f"Admin username: {admin.get_username()}")
            print(f"Admin role: {admin.get_role()}")
            print(f"Admin contact: {admin.get_email()}\t{admin.get_phoneNumber()}")
        else:
            print("Admin not found.")



