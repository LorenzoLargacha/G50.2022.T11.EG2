# Importamos el fichero json y la libreria uuid
import json
import uuid
# sacamos el import fuera
import re

from .VaccineMangementException import VaccineManagementException
from .VaccineRequest import VaccineRequest

class VaccineManager:
    def __init__(self):
        pass

    def ValidateGUID( self, GUID ):
        # CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        try:
            myUUID = uuid.UUID(GUID)
            myregex = re.compile(r'^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-'
                                 r'[0-9A-F]{12}$'
                                 , re.IGNORECASE)
            x = myregex.fullmatch(GUID)
            if not x:
                raise VaccineManagementException("Invalid UUID v4 format")
        # Definimos un error e como ValueError
        except ValueError as e:
            raise VaccineManagementException("Id received is not a UUID") from e
        return True


    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise VaccineManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise VaccineManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            Guid = DATA["id"]
            Zip = DATA["phoneNumber"]
            req = VaccineRequest(Guid, Zip)
        except KeyError as e:
            raise VaccineManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateGUID(Guid):
            raise VaccineManagementException("Invalid GUID")

        # Close the file
        return req