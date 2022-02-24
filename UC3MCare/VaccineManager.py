import json
from .VaccineMangementException import VaccineManagementException
from .VaccineRequest import VaccineRequest

class VaccineManager:
    def __init__(self):
        pass

    def ValidateGUID( self, GUID ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
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