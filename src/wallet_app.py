from typing import List
from .credit_card_form import CreditCardForm
from .credit_cards_list import CreditCardsList
from .dto import CreditCardInfo


class WalletApp():
    """This class orchestrates actions on app and proxies low level actions to relevant class"""

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.credit_card_form = CreditCardForm(self.browser)
        self.credit_card_list = CreditCardsList(self.browser)

    def load(self):
        self.browser.get(self.url)

    def fill_form(self, form_data: CreditCardInfo = None):
        if form_data.credit_card_number:
            self.credit_card_form.input_credit_card_number(
                form_data.credit_card_number)

        if form_data.expiration:
            self.credit_card_form.input_expiration(
                form_data.expiration)

        if form_data.street_address:
            self.credit_card_form.input_street_address(
                form_data.street_address)

        if form_data.city:
            self.credit_card_form.input_city(
                form_data.city)

        if form_data.state:
            self.credit_card_form.input_state(
                form_data.state)

        if form_data.postal_code:
            self.credit_card_form.input_postal_code(
                form_data.postal_code)

        if form_data.nickname:
            self.credit_card_form.input_nickname(
                form_data.nickname)

    def save_form(self):
        self.credit_card_form.click_on_save_button()

    def cancel_form(self):
        self.credit_card_form.click_on_cancel_button()

    def get_form_state(self) -> CreditCardInfo:
        form_state = CreditCardInfo(
            credit_card_number=self.credit_card_form.get_credit_card_number(),
            expiration=self.credit_card_form.get_expiration(),
            street_address=self.credit_card_form.get_street_address(),
            city=self.credit_card_form.get_city(),
            state=self.credit_card_form.get_state(),
            postal_code=self.credit_card_form.get_postal_code(),
            nickname=self.credit_card_form.get_nickname(),
        )

        return form_state

    def get_all_credit_cards(self) -> List[CreditCardInfo]:
        return self.credit_card_list.get_all_credit_cards()

    def click_on_add_credit_card(self):
        return self.credit_card_list.click_on_add_card()

    def set_credit_card_as_primary_by_four_digits(self, last_four_digits):
        self.credit_card_list.set_credit_card_as_primary_by_four_digits(
            last_four_digits)
