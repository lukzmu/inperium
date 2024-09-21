import yaml

from company.dto import Company
from company.mapper import CompanyMapper


class CompanyRepository:
    def __init__(self, data_path: str) -> None:
        self._data_path = data_path

    def get_companies(self) -> list[Company]:
        with open(self._data_path) as file:
            data = yaml.safe_load(stream=file)
            return [CompanyMapper.dict_to_dto(company=company) for company in data["items"]]


company_repository = CompanyRepository("data/company.yml")
