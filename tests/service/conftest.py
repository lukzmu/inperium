import pytest

from service.repository import ServiceRepository


@pytest.fixture
def service_repository():
    def _service_repository(data_path="dummy_path"):
        return ServiceRepository(data_path=data_path)

    return _service_repository


@pytest.fixture
def service_data():
    return {
        "items": [
            {"name": "Software solutions tailored to your business"},
            {"name": "Data-driven insights and product analytics"},
        ],
    }
