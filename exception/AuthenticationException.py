class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed. Incorrect username or password."):
        self.message = message
        super().__init__(self.message)
