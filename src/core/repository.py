import yaml

from core.dto import Contact
from core.mapper import ContactMapper


class ContactRepository:
    def __init__(self, data_path: str) -> None:
        self._data_path = data_path

    def get_contact(self) -> Contact:
        with open(self._data_path) as file:
            data = yaml.safe_load(stream=file)
            return ContactMapper.dict_to_dto(contact=data)


contact_repository = ContactRepository("data/contact.yml")
