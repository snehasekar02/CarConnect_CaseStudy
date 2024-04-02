class ReservationException(Exception):
    """Exception raised when there is a conflict with reservations."""

    def __init__(self, message="Reservation conflict: Vehicle already reserved"):
        self.message = message
        super().__init__(self.message)