import uuid

from Exceptions.app_exception import AppException


class Uuid_helper():
    
    @staticmethod
    def validate_request_uuid(id: uuid.UUID):
        if id is None or str(id) == '00000000-0000-0000-0000-000000000000':
            return False
        elif isinstance(id, uuid.UUID):
            return True
        else:
            return False


    @staticmethod
    def check_valid_uuid(id: uuid.UUID):
        if not Uuid_helper.validate_request_uuid(id):
            raise AppException("El ID proporcionado no es valido")