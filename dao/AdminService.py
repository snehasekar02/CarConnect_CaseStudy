from dao.IAdminService import IAdminService
from entity.Admin import Admin
from dao.DatabaseContext import DatabaseContext
from exception.AdminNotFoundException import AdminNotFoundException
from exception.InvalidInputException import InvalidInputException

def get_connection():
    return DatabaseContext.getConnection(r'D:\Hexaware\CarConnect\util\db.properties')

class AdminService(IAdminService):

    def get_admin_by_id(self, admin_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admin WHERE admin_id = ?", (admin_id,))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AdminNotFoundException("Admin with ID {} not found".format(admin_id))

            admin = Admin(*admin_data)
            return admin

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return None

    def get_admin_by_username(self, username):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admin WHERE Username= ?", (username,))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AdminNotFoundException("Admin with username {} not found".format(username))

            admin = Admin(*admin_data)
            return admin

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return None

    def register_admin(self, admin):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Admin (adminID, firstName, lastName, email, phoneNumber, username, password, role, joinDate)"
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (admin.get_adminID(), admin.get_firstName(), admin.get_lastName(), admin.get_email(),
                 admin.get_phoneNumber(),
                 admin.get_username(), admin.get_password(), admin.get_role(), admin.get_joinDate()))

            connection.commit()

            return True

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return False

    def update_admin(self, admin: Admin):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Admin SET firstName=?, lastName=?, email=?, phoneNumber=?,username=?,password=?,role=?,joinDate=? WHERE admin_id,=?",
                (Admin.firstName, Admin.lastName, Admin.email, Admin.phoneNumber, Admin.username, Admin.password,
                 Admin.role, Admin.joinDate, Admin.adminID,))
            connection.commit()

            return True

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return False

    def delete_admin(self, admin_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Admin WHERE admin_id=?", (admin_id,))
            connection.commit()
            return True

        except InvalidInputException:
            print("Required field is missing or has an incorrect format")

        except Exception as e:
            print("Error:", e)
            return False
