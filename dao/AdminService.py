from dao.IAdminService import IAdminService
from entity.Admin import  Admin
from dao.DatabaseContext import DatabaseContext
from exception import AdminNotFoundException
class AdminService(IAdminService):
    def __init__(self):
        self.database_context = DatabaseContext

    def get_admin_by_id(self, admin_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admin WHERE admin_id = ?", (admin_id,))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AdminNotFoundException("Admin with ID {} not found".format(admin_id))

            admin = Admin(*admin_data)
            return admin

        except Exception as e:
            print("Error:", e)
            return None



    def get_admin_by_username(self, username):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admin WHERE Username= ?", (username,))
            admin_data = cursor.fetchone()

            if not admin_data:
                raise AdminNotFoundException("Admin with username {} not found".format(username))

            admin = Admin(*admin_data)
            return admin

        except Exception as e:
            print("Error:", e)
            return None

    def register_admin(self, admin):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Admin (admin_id, firstName, lastName, email, phoneNumber,username,password,role,joinDate) VALUES (?, ?, ?, ?, ?,?,?,?,?)",
                (Admin.admin_id, Admin.firstName, Admin.lastName,Admin.email,Admin.phoneNumber,Admin.username,Admin.password,Admin.role,Admin.joinDate))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_admin(self, admin):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Admin SET firstName=?, lastName=?, email=?, phoneNumber=?,username=?,password=?,role=?,joinDate=? WHERE admin_id,=?",
                ( Admin.firstName, Admin.lastName,Admin.email,Admin.phoneNumber,Admin.username,Admin.password,Admin.role,Admin.joinDate,Admin.admin_id,))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def delete_admin(self, admin_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Admin WHERE admin_id=?", (admin_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False

