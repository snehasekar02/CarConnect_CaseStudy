from dao.AuthenticationService import AuthenticationService
from dao.AdminService import AdminService
from dao.CustomerService import CustomerService
from entity.Admin import Admin
from entity.Customer import Customer

authentication_service = AuthenticationService()


def handle_customer_actions(username):
    pass


def customer_workflow():
    customer_service = CustomerService()
    while True:
        print("Are you a new customer or an existing customer?")
        print("1. New Customer")
        print("2. Existing Customer")
        print("3. Quit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            last_cust_id = 0
            print("Customer Registration:")
            customer_id = last_cust_id + 1
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            email = input("Enter your email: ")
            phone_number = input("Enter your phone number: ")
            address = input("Enter your address: ")
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            registration_date = input("Enter your registration date: ")
            new_customer = Customer(customer_id, first_name, last_name, email, phone_number, address,
                                    username, password, registration_date)
            if customer_service.register_customer(new_customer):
                print("Registration successful!")
            else:
                print("Registration failed. Please try again.")
        elif choice == 2:
            print("Customer Login:")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authentication_service.authenticate_customer(username, password):
                print("Login successful!")
                # Proceed with actions a logged-in customer can perform
                # For example, you can call a function to handle reservations
                handle_customer_actions(username)
            else:
                print("Login failed. Incorrect username or password.")
        elif choice == 3:
            print("Exiting Customer...")
            break
        else:
            print("Invalid choice")


def handle_admin_actions(username):
    pass


def admin_workflow():
    while True:
        print("Welcome to CarConnect - Car Rental Platform")
        print("1. Admin Registration")
        print("2. Admin Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            last_admin_id = 100  # Start with admin ID 101
            admin_id = last_admin_id + 1
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter role: ")
            join_date = input("Enter join date: ")
            admin = Admin(admin_id, first_name, last_name, email, phone_number, username, password, role, join_date)

            if AdminService.register_admin(admin):
                print("Registration successful!")
            else:
                print("Registration failed. Please try again.")
        elif choice == '2':
            print("Admin Login:")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authentication_service.authenticate_admin(username, password):
                print("Login successful!")

                # Proceed with actions a logged-in admin can perform
                handle_admin_actions(username)
            else:
                print("Login failed. Incorrect username or password.")
        elif choice == '3':
            print("Exiting CarConnect. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main():
    print("Welcome to the Reservation System")
    print("Are you a customer or an admin?")
    print("1. Customer")
    print("2. Admin")
    user_type = int(input("Enter your choice: "))
    if user_type == 1:
        customer_workflow()
    elif user_type == 2:
        admin_workflow()
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
