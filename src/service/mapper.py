from service.dto import Service


class ServiceMapper:
    @staticmethod
    def dict_to_dto(service: dict[str, str | int]) -> Service:
        return Service(name=service["name"])
