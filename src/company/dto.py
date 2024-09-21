from dataclasses import dataclass


@dataclass(frozen=True)
class Company:
    name: str
    icon: str
