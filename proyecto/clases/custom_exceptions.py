class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        
class NonExistentCollectionError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        
class NotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)