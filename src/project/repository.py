import yaml

from project.dto import Project
from project.mapper import ProjectMapper


class ProjectRepository:
    def __init__(self, data_path: str) -> None:
        self._data_path = data_path

    def get_projects(self) -> list[Project]:
        with open(self._data_path) as file:
            data = yaml.safe_load(stream=file)
            return [ProjectMapper.dict_to_dto(project=project) for project in data["items"]]


project_repository = ProjectRepository("data/project.yml")
