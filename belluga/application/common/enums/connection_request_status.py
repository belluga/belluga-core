import enum
 
# creating enumerations using class
class ConnectionRequestStatus(enum.Enum):
    received = "received"
    error = "error"
    processed = "processed"
    ready = "ready"
    retry = "retry"
    invalid = "invalid"