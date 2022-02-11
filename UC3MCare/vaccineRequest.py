import json
from datetime import datetime
import pandas

class VaccineRequest:
    def __init__( self, idcode, phoneNumber ):
        self.__phoneNumber = phoneNumber
        self.__idcode = idcode
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "VaccineRequest:" + json.dumps(self.__dict__)

    @property
    def Phone( self ):
        return self.__phoneNumber
    @Phone.setter
    def Phone( self, value ):
        self.__phoneNumber = value

    @property
    def idDocument(self):
        return self.__idcode
    @idDocument.setter
    def idDocument(self,value):
        self.__idcode = value
