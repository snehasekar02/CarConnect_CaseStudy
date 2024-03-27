from dao.IReservationService import IReservationService
from entity.Reservation import Reservation
from dao.DatabaseContext import DatabaseContext
from exception.ReservationException import ReservationException


def get_connection():
    return DatabaseContext.getConnection(r'D:\Hexaware\CarConnect\util\db.properties')


class ReservationService(IReservationService):
    def get_reservation_by_id(self, reservationID):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE reservationID = %s", (reservationID,))
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
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Reservation WHERE customerID = %s", (customer_id,))
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
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "INSERT INTO Reservation (reservationID, customerID, vehicleID, startDate, EndDate,TotalCost,Status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (reservation.get_reservationID(), reservation.get_customerID(), reservation.get_vehicleID(),
                 reservation.get_startDate(), reservation.get_endDate(), reservation.get_totalCost(),
                 reservation.get_status()))

            connection.commit()

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def update_reservation(self, reservation):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute(
                "UPDATE  Reservation SET customerID=%s, vehicleID=%s, startDate=%s, endDate=%s,totalCost=%s,status=%s WHERE reservationID=%s",
                (reservation.get_customerID(), reservation.get_vehicleID(), reservation.get_startDate(),
                 reservation.get_endDate(), reservation.get_totalCost(), reservation.get_status(),
                 reservation.get_reservationID()))
            connection.commit()
            print("Reservation Updated!!")

            return True

        except Exception as e:
            print("Error:", e)
            return False

    def cancel_reservation(self, reservation_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Reservation WHERE reservationID=%s", (reservation_id,))
            connection.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False
