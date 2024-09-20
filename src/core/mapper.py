from core.dto import Contact


class ContactMapper:
    @staticmethod
    def dict_to_dto(contact: dict[str, str | int]) -> Contact:
        return Contact(
            name=contact["name"],
            email=contact["email"],
            vat=contact["vat"],
            regon=int(contact["regon"]),
        )
