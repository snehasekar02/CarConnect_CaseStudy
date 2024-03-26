from exception.AuthenticationException import AuthenticationException
class AuthenticationService:
    def __init__(self, database_context):
        self.database_context = database_context

    def authenticate_user(self, username, password):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Customer WHERE username = ? AND password = ?", (username, password))
            customer_data = cursor.fetchone()

            if not customer_data:
                raise AuthenticationException("Incorrect Username or Password...")
                return False

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def authenticate_customer(self, username, password):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Admin WHERE username = ? AND password = ?", (username, password))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AuthenticationException("Incorrect Username or Password...")
                return False

            return True

        except Exception as e:
            print("Error:", e)
            return False
