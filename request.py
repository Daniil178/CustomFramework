"""
    Модель ответа пользователю
"""
from typing import Any
from dataclasses import dataclass


@dataclass
class response:
    data: dict[Any]
    query_params: dict[str, str]
    method: str
    content_type: str
