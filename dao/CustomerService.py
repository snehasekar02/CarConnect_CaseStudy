from dao.ICustomerService import ICustomerService
from entity.Customer import  Customer
from dao.DatabaseContext import DatabaseContext
from exception.CustomerNotFoundException import CustomerNotFoundException


class CustomerService(ICustomerService):
    def __init__(self, database_context):
        self.database_context = DatabaseContext

    def get_customer_by_id(self, customer_id):

        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE customer_id = ?", (customer_id,))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise CustomerNotFoundException("Admin with ID {} not found".format(customer_id))

            customer = Customer(*customer_data)
            return customer

        except Exception as e:
            print("Error:", e)
            return None

    def get_customer_by_username(self, username):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE Username= ?", (username,))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise CustomerNotFoundException("Admin with username {} not found".format(username))

            customer = Customer(*customer_data)
            return customer

        except Exception as e:
            print("Error:", e)
            return None

    def register_customer(self, customer):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Customer (customer_id, firstName, lastName, email, phoneNumber,username,password,role,joinDate) VALUES (?, ?, ?, ?, ?,?,?,?,?)",
                (customer.customer_id, customer.firstName, customer.lastName, customer.email, customer.phoneNumber, customer.username,
                 customer.password, customer.role, customer.joinDate))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_customer(self, customer):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Customer SET firstName=?, lastName=?, email=?, phoneNumber=?,username=?,password=?,role=?,joinDate=? WHERE customer_id,=?",
                (customer.firstName, customer.lastName, customer.email, customer.phoneNumber, customer.username, customer.password,
                 customer.role, customer.joinDate, customer.customer_id,))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def delete_customer(self, customer_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Customer WHERE customer_id=?", (customer_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False
