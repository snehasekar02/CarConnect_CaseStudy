from VehicleService import VehicleService
from CustomerService import CustomerService
from ReservationService import ReservationService
from AdminService import AdminService
class ReportGenerator:
    def __init__(self, database_context):
        self.database_context = database_context

    def generate_report(self):
        ch=int(input(("Report Generation\n1.By Vehicle\n2.By Customer\n3.By Reservation\n4.By Admin")))
        if ch==1:
            Vehicle_ID=int(input("Enter Vehicle ID: "))
            vehicle=VehicleService.get_vehicle_by_id(Vehicle_ID)
            print(f"ID: {vehicle.vehicleID}\nRegistration ID: {vehicle.registrationNumber},\nVehicle model : {vehicle.model},\n Vehicle color: {vehicle.color},\n Vehicle dailyrate: {vehicle.dailyRate},\nVehicle availability: {vehicle.availability}")
        elif ch==2:
            Customer_ID=int(input("Enter Customer ID: "))
            customer=CustomerService.get_customer_by_id(Customer_ID)
            print(f"\nCustomer ID {customer.get_customer_id()}\nName: {customer.get_first_name()+customer.get_last_name()}\nUsername: {customer.get_username()}\nEmail: {customer.set_email()}\nPhone_number: {customer.get_phone_number()}\nAddress: {customer.get_address()}")
        elif ch==3:
            Reservaion_ID=int(input("Reservation ID: "))
            reservation=ReservationService.get_reservation_by_id(Reservaion_ID)
            print(f"\nReservation ID: {reservation.reservationID}\nCustomer ID: {reservation.customerID}\nVehicle: {reservation.vehicleID}\nStatus:{reservation.status},\nCost: {reservation.totalCost}")
        elif ch==4:
            Admin_ID=int(input("Enter Admin ID: "))
            admin=AdminService.get_admin_by_id(Admin_ID)
            print(f"\nAdmin id: {admin.adminID}\nadmin name: {admin.firstName+admin.lastName}\nadmin username:{admin.username}\nadmin role: {admin.role}\nadmin contact: {admin.email}\t{admin.phoneNumber}")






