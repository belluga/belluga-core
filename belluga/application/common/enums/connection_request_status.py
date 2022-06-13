import enum
 
# creating enumerations using class
class ConnectionRequestStatus(enum.Enum):
    received = "received"
    error = "error"
    processed = "processed"
    retry = "retry"
    invalid = "invalid"
    valid = "valid"