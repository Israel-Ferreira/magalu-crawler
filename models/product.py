from dataclasses import dataclass

import json

@dataclass
class Product:
    id: str
    name: str
    url: str
    price: float


    def __str__(self) -> str:
        return json.dumps(self.__dict__)


    