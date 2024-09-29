import json

from core.dto import Contact


class TestContactRepository:
    def test_contact_repository_constructor(self, contact_repository):
        data_path = "data/contact.yml"
        repository = contact_repository(data_path=data_path)

        assert repository._data_path == data_path

    def test_contact_returns_corrent_data(self, contact_repository, contact_data, mocker):
        mocked_data = mocker.mock_open(read_data=json.dumps(contact_data))
        mocker.patch("builtins.open", mocked_data)

        result = contact_repository().get_contact()

        assert type(result) is Contact
