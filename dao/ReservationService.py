from dao.IReservationService import IReservationService
from entity.Reservation import  Reservation
from dao.DatabaseContext import DatabaseContext


class ReservationService(IReservationService):
    def __init__(self, database_context):
        self.database_context = DatabaseContext

    def get_reservation_by_id(self, reservationID):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE reservationID = ?", (reservationID,))
            reservation_data = cursor.fetchone()

            if not reservation_data:
                raise ReservationException("Reservation with ID {} not found".format(reservationID))

            reservation = Reservation(*reservation_data)
            return reservation

        except Exception as e:
            print("Error:", e)
            return None

    def get_reservations_by_customer_id(self, customer_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE customerID = ?", (customer_id,))
            reservation_data = cursor.fetchall()

            if not reservation_data:
                raise ReservationException("Reservation with ID {} not found".format(customer_id))

            reservation = Reservation(*reservation_data)
            return reservation

        except Exception as e:
            print("Error:", e)
            return None

    def create_reservation(self, reservation):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Reservation (reservationID, customerID, vehicleID, startDate, EndDate,TotalCost,Status) VALUES (?, ?, ?, ?, ?,?,?)",
                (Reservation.reservationID, Reservation.customerID,Reservation.vehicleID,Reservation.startDate,Reservation.endDate,Reservation.totalCost,Reservation.status))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_reservation(self, reservation):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Reservation SET customerID=?, vehicleID=?, startDate=?, endDate=?,totalCost=?,status=? WHERE reservationID,=?",
                (Reservation.customerID,Reservation.vehicleID,Reservation.startDate,Reservation.endDate,Reservation.totalCost,Reservation.status, Reservation.reservationID,))
            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def cancel_reservation(self, reservation_id):
        try:
            connection = self.database_context.getConnection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Reservation WHERE reservationID=?", (reservation_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False


