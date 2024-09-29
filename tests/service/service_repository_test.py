import json


class TestServiceRepository:
    def test_service_repository_constructor(self, service_repository):
        data_path = "data/service.yml"
        repository = service_repository(data_path=data_path)

        assert repository._data_path == data_path

    def test_service_list_returns_correct_service_count(Self, service_repository, service_data, mocker):
        mocked_data = mocker.mock_open(read_data=json.dumps(service_data))
        mocker.patch("builtins.open", mocked_data)

        result = service_repository().get_services()

        assert len(result) == len(service_data["items"])
