from dataclasses import dataclass
from typing import Callable

@dataclass
class Command:
    name: str
    description: str
    handler: Callable