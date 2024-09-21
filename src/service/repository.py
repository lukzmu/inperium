import yaml

from service.dto import Service
from service.mapper import ServiceMapper


class ServiceRepository:
    def __init__(self, data_path: str) -> None:
        self._data_path = data_path

    def get_services(self) -> list[Service]:
        with open(self._data_path) as file:
            data = yaml.safe_load(stream=file)
            return [ServiceMapper.dict_to_dto(service=service) for service in data["items"]]


service_repository = ServiceRepository("data/service.yml")
