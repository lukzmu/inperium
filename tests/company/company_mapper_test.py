from company.dto import Company
from company.mapper import CompanyMapper


class TestCompanyMapper:
    def test_company_mapper_parses_data_correctly(self, company_data):
        selected_company = company_data["items"][0]

        result = CompanyMapper.dict_to_dto(company=selected_company)

        assert type(result) == Company
        assert result.name == selected_company["name"]
        assert result.icon == selected_company["icon"]
