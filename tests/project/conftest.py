import pytest

from project.repository import ProjectRepository


@pytest.fixture
def project_repository():
    def _project_repository(data_path="dummy_path"):
        return ProjectRepository(data_path=data_path)

    return _project_repository


@pytest.fixture
def project_data():
    return {
        "items": [
            {
                "name": "IoT Emergency Lightning System",
                "icon": "iot_lightning.png",
            },
            {
                "name": "Medical Knowledge Base",
                "icon": "medical_knowledge_base.png",
            },
        ],
    }
