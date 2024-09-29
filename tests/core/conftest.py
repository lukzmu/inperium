import pytest

from core.repository import ContactRepository


@pytest.fixture
def contact_repository():
    def _contact_repository(data_path="dummy_path"):
        return ContactRepository(data_path=data_path)

    return _contact_repository


@pytest.fixture
def contact_data():
    return {
        "name": "INPERIUM",
        "email": "hello@inperium.eu",
        "vat": "PL7393659738",
        "regon": 380660414,
    }
