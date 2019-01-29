import enum


class DataType(enum):
    BOOLEAN = 'boolean'
    BYTE = 'byte'
    SHORT = 'short'
    INT = 'int'
    LONG = 'long'
    UBYTE = 'ubyte'
    USHORT = 'ushort'
    UINT = 'uint'
    ULONG = 'ulong'
    FLOAT = 'float'
    DOUBLE = 'double'
    ASCII_STRING = 'asci_string'
    UTF_STRING = 'utf_string'
    OTHER = 'other'
    DISCARD = 'discard'
    MIXED = 'mixed'

    @property
    def is_integral_type(self):
        if self in (
                DataType.BYTE, DataType.UBYTE, DataType.SHORT, DataType.USHORT, DataType.INT, DataType.UINT,
                DataType.LONG,
                DataType.ULONG):
            return True
        else:
            return False

    @property
    def is_number_type(self):
        if DataType.is_integral_type:
            return True
        elif self in (DataType.FLOAT, DataType.DOUBLE):
            return True
        else:
            return False

    @property
    def is_text_type(self):
        if self in (DataType.ASCII_STRING, DataType.UTF_STRING):
            return True
        else:
            return False
