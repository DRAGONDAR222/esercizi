from enum import Enum

class StatusEnum(str, Enum):
    RICEVUTO = "received"
    DIAGNOSING = "diagnosing"
    REPAIRING = "repairing"
    READY = "ready"
    DELIVERED = "delivered"

