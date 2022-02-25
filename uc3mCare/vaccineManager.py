# Importamos el fichero json y la libreria uuid
import json
import uuid
# sacamos el import fuera
import re

from .vaccineMangementException import vaccineManagementException
from .vaccineRequest import vaccineRequest

class vaccineManager:
    def __init__(self):
        pass

    def ValidateGUID(self, GUID):
        # CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        try:
            MYUUID = uuid.UUID(GUID)
            MYREGEX = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                                 r'[0-9A-F]{12}$'
                                 , re.IGNORECASE)
            X__ = MYREGEX.fullmatch(GUID)
            if not X__:
                raise vaccineManagementException("Invalid UUID v4 format")
        # Definimos un error e como ValueError
        except ValueError as ERROR:
            raise vaccineManagementException("Id received is not a UUID") from ERROR

        return True


    def ReadAccessRequestFromJSON(self, fi):

        try:
            with open(fi) as FILE:
                DATA = json.load(FILE)
        except FileNotFoundError as ERROR:
            raise vaccineManagementException("Wrong file or file path") from ERROR
        except json.JSONDecodeError as ERROR:
            raise vaccineManagementException("JSON Decode Error - Wrong JSON Format") from ERROR

        try:
            GUID = DATA["id"]
            ZIP = DATA["phoneNumber"]
            REQ = vaccineRequest(GUID, ZIP)
        except KeyError as ERROR:
            raise vaccineManagementException("JSON Decode Error - Invalid JSON Key") from ERROR
        if not self.ValidateGUID(GUID):
            raise vaccineManagementException("Invalid GUID")

        # Close the file
        return REQ
