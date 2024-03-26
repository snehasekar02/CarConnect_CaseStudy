class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None,
                 phone_number=None, address=None, username=None, password=None, registration_date=None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__username = username
        self.__password = password
        self.__registration_date = registration_date

    def authenticate(self, password):
        if len(password)>8 and  any(char.isupper() for char in password) and any(char.isdigit() for char in password) :
            return self.__password == password
        else:
            print("Invalid Password!!")

    # Getters and setters
    def get_customer_id(self):
        return self.__customer_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_registration_date(self):
        return self.__registration_date

    def set_registration_date(self, registration_date):
        self.__registration_date = registration_date

    def print_info(self):
        print("Customer ID:", self.__customer_id)
        print("First Name:", self.__first_name)
        print("Last Name:", self.__last_name)
        print("Email:", self.__email)
        print("Phone Number:", self.__phone_number)
        print("Address:", self.__address)
        print("Username:", self.__username)
        # Do not print password for security reasons
        print("Registration Date:", self.__registration_date)