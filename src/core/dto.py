from dataclasses import dataclass


@dataclass(frozen=True)
class Contact:
    name: str
    email: str
    vat: str
    regon: int
