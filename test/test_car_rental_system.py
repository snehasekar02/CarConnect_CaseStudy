import unittest
from dao.AuthenticationService import AuthenticationService
from dao.CustomerService import CustomerService
from dao.VehicleService import VehicleService
from entity.Customer import Customer
from entity.Vehicle import Vehicle


class TestCarRentalSystem(unittest.TestCase):

    def setUp(self):
        self.auth_service = AuthenticationService()
        self.customer_service = CustomerService()
        self.vehicle_service = VehicleService()

    def test_customer_authentication_with_invalid_credentials(self):
        username = "sneha"
        password = "sneha"
        self.assertFalse(self.auth_service.authenticate_customer(username, password))

    def test_updating_customer_information(self):
        # Test updating customer information
        customer_id = 1  # Assuming this customer ID exists in the database
        updated_firstname = 'sneha'
        updated_lastname = 'c'
        updated_email = "csneha@mail.com"
        updated_phone_number = "9025309801"
        updated_address = "Trichy"
        updated_username = 'sneha_25'
        updated_password = 'Sneha@123'
        updated_registration_date = '2024-03-27'
        updated_customer = Customer(customer_id, updated_firstname, updated_lastname, updated_email,
                                    updated_phone_number, updated_address, updated_username, updated_password, updated_registration_date)
        self.assertTrue(self.customer_service.update_customer(updated_customer))

    def test_adding_new_vehicle(self):
        # Test adding a new vehicle
        vehicle = Vehicle(vehicleID=1003, model="Benz", make="India", year=2021, color="Blue",
                          registrationNumber="TN 45 BC 1294", availability=1, dailyRate=220.00)
        self.assertTrue(self.vehicle_service.add_vehicle(vehicle))

    def test_updating_vehicle_details(self):
        # Test updating vehicle details
        vehicle_id = 1001  # Assuming this vehicle ID exists in the database
        updated_model = "Audi"
        updated_make = "India"
        updated_year = 2023
        updated_color = "Black"
        updated_registration_number = 'TN 48 YY 7865'
        updated_availability = 1
        updated_daily_rate = 110.00
        updated_vehicle = Vehicle(vehicle_id, updated_model, updated_make,updated_year, updated_color,
                                  updated_registration_number, updated_availability, updated_daily_rate)
        self.assertTrue(self.vehicle_service.update_vehicle(updated_vehicle))

    def test_getting_list_of_available_vehicles(self):
        # Test getting a list of available vehicles
        available_vehicles = self.vehicle_service.get_available_vehicles()
        self.assertTrue(isinstance(available_vehicles, list))


'''
    def test_getting_list_of_all_vehicles(self):
        # Test getting a list of all vehicles
        all_vehicles = self.vehicle_service.get_all_vehicles()
        self.assertTrue(isinstance(all_vehicles, list))
'''
if __name__ == '__main__':
    unittest.main()
