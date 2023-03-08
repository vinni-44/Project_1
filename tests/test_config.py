




class NotInRange(Exception):
    def __init__(self,message = "Not in Range"):
        self.message = message
        super().__init__(self.message)