from core.dto import Contact
from core.mapper import ContactMapper


class TestContactMapper:
    def test_contact_mapper_parses_data_correctly(self, contact_data):
        result = ContactMapper.dict_to_dto(contact=contact_data)

        assert type(result) is Contact
        assert result.name == contact_data["name"]
        assert result.email == contact_data["email"]
        assert result.vat == contact_data["vat"]
        assert result.regon == contact_data["regon"]
