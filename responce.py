"""
    Модель запроса от пользователя
"""
from typing import Any
from dataclasses import dataclass
from status import HTTP_STATUS


@dataclass
class response:
    data: dict[Any]
    status: HTTP_STATUS
    headers: dict[Any]
    content_type: str
