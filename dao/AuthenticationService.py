from dao.DatabaseContext import DatabaseContext
from exception.AuthenticationException import AuthenticationException


def get_connection():
    return DatabaseContext.getConnection(r'D:\Hexaware\CarConnect\util\db.properties')


class AuthenticationService:
    def authenticate_customer(self, username, password):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE username = %s AND password = %s", (username, password))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise AuthenticationException("Incorrect Username or Password...")

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def authenticate_admin(self, username, password):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Admin WHERE username = ? AND password = ?", (username, password))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AuthenticationException("Incorrect Username or Password...")

            return True

        except Exception as e:
            print("Error:", e)
            return False
