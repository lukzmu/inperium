from dataclasses import dataclass


@dataclass(frozen=True)
class Service:
    name: str
