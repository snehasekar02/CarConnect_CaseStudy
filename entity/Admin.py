class Admin:
    def __init__(self, adminID, firstName, lastName, email, phoneNumber, username, password, role, joinDate):
        self.__adminID = adminID
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__username = username
        self.__password = password
        self.__role = role
        self.__joinDate = joinDate

    def get_adminID(self):
        return self.__adminID

    def set_adminID(self, value):
        self.__adminID = value

    def get_firstName(self):
        return self.__firstName

    def set_firstName(self, value):
        self.__firstName = value

    def get_lastName(self):
        return self.__lastName

    def set_lastName(self, value):
        self.__lastName = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email = value

    def get_phoneNumber(self):
        return self.__phoneNumber

    def set_phoneNumber(self, value):
        self.__phoneNumber = value

    def get_username(self):
        return self.__username

    def set_username(self, value):
        self.__username = value

    def get_password(self):
        return self.__password

    def set_password(self, value):
        self.__password = value

    def get_role(self):
        return self.__role

    def set_role(self, value):
        self.__role = value

    def get_joinDate(self):
        return self.__joinDate

    def set_joinDate(self, value):
        self.__joinDate = value

    def authenticate(self, enteredPassword):
        return self.__password == enteredPassword

    def print_info(self):
        print("Admin ID:", self.__adminID)
        print("First Name:", self.__firstName)
        print("Last Name:", self.__lastName)
        print("Email:", self.__email)
        print("Phone Number:", self.__phoneNumber)
        print("Username:", self.__username)
        # Do not print password for security reasons
        print("Role:", self.__role)
        print("Join Date:", self.__joinDate)
