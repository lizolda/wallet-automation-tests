import re
from selenium.webdriver.common.by import By
from typing import List
from .dto import CreditCardInfo


class CreditCardsList():
    """This class holds low level logic related to the cards list"""

    CREDIT_CARD_LIST_ITEM_SELECTOR = (
        By.XPATH, "/html/body/div/div/div[1]/div[contains(@class, 'MuiPaper-elevation') and not(contains(@class, 'MuiCollapse-hidden'))]")

    CREDIT_CARD_DIGITS_RELATIVE_SELECTOR = (
        By.XPATH, "./div[1]/div[1]/div/p/strong")

    CREDIT_CARD_DIGITS_WITH_PRIMARY_TEXT_RELATIVE_SELECTOR = (
        By.XPATH, "./div[1]/div[1]/div")

    NICKNAME_RELATIVE_SELECTOR = (
        By.XPATH, "./div[1]/div[1]/span")

    EXPIRATION_RELATIVE_SELECTOR = (
        By.XPATH, "./div[1]/div[2]")

    BILLING_ADDRESS_RELATIVE_SELECTOR = (
        By.XPATH, "./div[2]/div[1]/p[2]")

    SET_AS_PRIMARY_BUTTON_RELATIVE_SELECTOR = (
        By.XPATH, "./div[2]/div[2]/button[1]")

    ADD_CARD_BUTTON_SELECTOR = (
        By.XPATH, "/html/body/div/div/div[1]/button")

    def __init__(self, browser):
        self.browser = browser

    def _get_all_credit_cards_list_elements(self):
        credit_cards_elements = self.browser.find_elements(
            *self.CREDIT_CARD_LIST_ITEM_SELECTOR
        )

        return credit_cards_elements

    def _parse_credit_card_element(self, credit_card_element):
        credit_card_element.click()

        credit_card_last_four_digits_element = credit_card_element.find_element(
            *self.CREDIT_CARD_DIGITS_RELATIVE_SELECTOR)

        credit_card_last_four_digits = credit_card_last_four_digits_element.text

        nick_name_element = credit_card_element.find_element(
            *self.NICKNAME_RELATIVE_SELECTOR)

        expiration_element = credit_card_element.find_element(
            *self.EXPIRATION_RELATIVE_SELECTOR)

        address_element = credit_card_element.find_element(
            *self.BILLING_ADDRESS_RELATIVE_SELECTOR)

        address = address_element.text.split(", ")

        card_title_element = credit_card_element.find_element(
            *self.CREDIT_CARD_DIGITS_WITH_PRIMARY_TEXT_RELATIVE_SELECTOR)

        card_is_primary = bool(re.match(r".*Primary", card_title_element.text))

        return CreditCardInfo(
            credit_card_number=credit_card_last_four_digits,
            nickname=nick_name_element.text,
            expiration=expiration_element.text,
            street_address=address[0],
            city=address[1],
            state=address[2],
            is_primary=card_is_primary
        )

    def get_all_credit_cards(self) -> List[CreditCardInfo]:
        results = []

        for credit_card_element in self._get_all_credit_cards_list_elements():
            parsed_credit_card = self._parse_credit_card_element(
                credit_card_element)

            results.append(parsed_credit_card)

        return results

    def set_credit_card_as_primary_by_four_digits(self, last_four_digits):
        for credit_card_element in self._get_all_credit_cards_list_elements():

            parsed_credit_card = self._parse_credit_card_element(
                credit_card_element
            )

            if parsed_credit_card.credit_card_number == last_four_digits:
                self._set_credit_card_as_primary(credit_card_element)

    def _set_credit_card_as_primary(self, credit_card_element):
        set_as_primary_button = credit_card_element.find_element(
            *self.SET_AS_PRIMARY_BUTTON_RELATIVE_SELECTOR)

        set_as_primary_button.click()

    def click_on_add_card(self):
        add_card_button = self.browser.find_element(
            *self.ADD_CARD_BUTTON_SELECTOR)

        add_card_button.click()
