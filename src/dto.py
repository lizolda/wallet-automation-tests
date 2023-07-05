from dataclasses import dataclass


@dataclass
class CreditCardInfo:
    """Class that holds credit card info."""

    credit_card_number: str | None = None
    expiration: str | None = None
    is_primary: bool | None = False
    street_address: str | None = None
    city: str | None = None
    state: str | None = None
    postal_code: int | None = None
    nickname: str | None = ""
