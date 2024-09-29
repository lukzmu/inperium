import json


class TestProjectRepository:
    def test_project_repository_constructor(self, project_repository):
        data_path = "data/project.yml"
        repository = project_repository(data_path=data_path)

        assert repository._data_path == data_path

    def test_project_list_returns_correct_project_count(self, project_repository, project_data, mocker):
        mocked_data = mocker.mock_open(read_data=json.dumps(project_data))
        mocker.patch("builtins.open", mocked_data)

        result = project_repository().get_projects()

        assert len(result) == len(project_data["items"])
