from company.dto import Company


class CompanyMapper:
    @staticmethod
    def dict_to_dto(company: dict[str, str]) -> Company:
        return Company(
            name=company["name"],
            icon=company["icon"],
        )
