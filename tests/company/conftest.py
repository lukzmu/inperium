import pytest

from company.repository import CompanyRepository


@pytest.fixture
def company_repository():
    def _company_repository(data_path="dummy_path"):
        return CompanyRepository(data_path=data_path)

    return _company_repository


@pytest.fixture
def company_data():
    return {
        "items": [
            {
                "name": "INPERIUM",
                "icon": "inperium.svg",
            },
            {
                "name": "Apple",
                "icon": "apple.svg",
            },
        ],
    }
