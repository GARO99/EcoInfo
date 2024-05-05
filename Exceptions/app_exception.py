from typing import Any

class AppException(Exception):
    def __init__(self, detail: Any = None) -> None:
        super().__init__(detail)