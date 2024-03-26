import pyodbc
from util.PropertyUtil import SqlConnection


class DatabaseContext:
    @staticmethod
    def getConnection():
        connection = None
        try:
            dbname = SqlConnection.getDatabaseName('util/db.properties')
            connection = pyodbc.connect(f'Driver={{SQL Server}};'
                                        f'Server=SQLEXPRESS;'
                                        f'Database={dbname};'
                                        f'Trusted_Connection=yes;')
        except Exception as e:
            print("Connection failed:", str(e))
        return connection

#DESKTOP-QRH50KR\SQLEXPRESS
