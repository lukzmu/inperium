from project.dto import Project


class ProjectMapper:
    @staticmethod
    def dict_to_dto(project: dict[str, str]) -> Project:
        return Project(
            name=project["name"],
            icon=project["icon"],
        )
