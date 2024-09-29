from service.dto import Service
from service.mapper import ServiceMapper


class TestServiceMapper:
    def test_service_mapper_parses_data_correctly(self, service_data):
        selected_service = service_data["items"][0]

        result = ServiceMapper.dict_to_dto(service=selected_service)

        assert type(result) is Service
        assert result.name == selected_service["name"]
