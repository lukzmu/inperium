import json


class TestCompanyRepository:
    def test_company_repository_constructor(self, company_repository):
        data_path = "data/company.yml"
        repository = company_repository(data_path=data_path)

        assert repository._data_path == data_path

    def test_company_list_returns_correct_company_count(self, company_repository, company_data, mocker):
        mocked_data = mocker.mock_open(read_data=json.dumps(company_data))
        mocker.patch("builtins.open", mocked_data)

        result = company_repository().get_companies()

        assert len(result) == len(company_data["items"])
