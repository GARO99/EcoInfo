import re


class Validate_helper():
    
    @staticmethod
    def validate_email(email: str)-> bool:
        return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$',email.lower())