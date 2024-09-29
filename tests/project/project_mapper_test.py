from project.dto import Project
from project.mapper import ProjectMapper


class TestProjectMapper:
    def test_project_mapper_parses_data_correctly(self, project_data):
        selected_project = project_data["items"][0]

        result = ProjectMapper.dict_to_dto(project=selected_project)

        assert type(result) is Project
        assert result.name == selected_project["name"]
        assert result.icon == selected_project["icon"]
