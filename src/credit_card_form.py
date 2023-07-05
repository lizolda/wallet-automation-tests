from selenium.webdriver.common.by import By


class CreditCardForm():
    """This class holds low level logic related to the card creation form"""

    CREDIT_CARD_INPUT_SELECTOR = (
        By.XPATH, '//*[@id="profile_billing_cc_test"]')

    EXPIRATION_INPUT_SELECTOR = (
        By.XPATH, '//*[@id="profile_billing_expires"]')

    STREET_ADDRESS_INPUT_SELECTOR = (
        By.XPATH, '//*[@id="profile_billing_street"]')

    CITY_INPUT_SELECTOR = (
        By.XPATH, '//*[@id="profile_billing_city"]')

    NICKNAME_INPUT_SELECTOR = (
        By.XPATH, '//*[@id="profile_nickname"]')

    STATE_INPUT_SELECTOR = (
        By.XPATH, '//*[@id="profile_billing_state"]')

    POSTAL_CODE_SELECTOR = (
        By.XPATH, '//*[@id="profile_billing_postal_code"]')

    SAVE_BUTTON_SELECTOR = (
        By.XPATH, '//button[text()="Save"]')

    CANCEL_BUTTON_SELECTOR = (
        By.XPATH, '//button[text()="Cancel"]')

    def __init__(self, browser):
        self.browser = browser

    def get_credit_card_number(self):
        credit_card_input = self.browser.find_element(
            *self.CREDIT_CARD_INPUT_SELECTOR
        )

        return credit_card_input.get_attribute("value").strip()

    def input_credit_card_number(self, credit_card_number):
        credit_card_input = self.browser.find_element(
            *self.CREDIT_CARD_INPUT_SELECTOR
        )

        credit_card_input.send_keys(credit_card_number)

    def input_expiration(self, expiration):
        expiration_input = self.browser.find_element(
            *self.EXPIRATION_INPUT_SELECTOR
        )

        expiration_input.send_keys(expiration)

    def get_expiration(self):
        expiration_input = self.browser.find_element(
            *self.EXPIRATION_INPUT_SELECTOR
        )

        return expiration_input.get_attribute("value")

    def input_street_address(self, street_address):
        street_address_input = self.browser.find_element(
            *self.STREET_ADDRESS_INPUT_SELECTOR)

        street_address_input.send_keys(street_address)

    def get_street_address(self):
        street_address_input = self.browser.find_element(
            *self.STREET_ADDRESS_INPUT_SELECTOR)

        return street_address_input.get_attribute('value')

    def input_city(self, city):
        city_input = self.browser.find_element(
            *self.CITY_INPUT_SELECTOR)

        city_input.send_keys(city)

    def get_city(self):
        city_input = self.browser.find_element(
            *self.CITY_INPUT_SELECTOR)

        return city_input.get_attribute("value")

    def input_state(self, state):
        state_input = self.browser.find_element(
            *self.STATE_INPUT_SELECTOR)

        state_input.click()

        state_element = self.browser.find_element(
            By.XPATH, f'//li[@data-value="{state}"]')

        state_element.click()

    def get_state(self):
        state_input = self.browser.find_element(
            *self.STATE_INPUT_SELECTOR)

        return state_input.text

    def input_postal_code(self, postal_code):
        postal_code_input = self.browser.find_element(
            *self.POSTAL_CODE_SELECTOR)

        postal_code_input.send_keys(postal_code)

    def get_postal_code(self):
        postal_code_input = self.browser.find_element(
            *self.POSTAL_CODE_SELECTOR)

        raw_postal_code = postal_code_input.get_attribute("value")

        if raw_postal_code:
            return int(raw_postal_code)
        return None

    def input_nickname(self, nickname):
        nickname_input = self.browser.find_element(
            *self.NICKNAME_INPUT_SELECTOR)

        nickname_input.send_keys(nickname)

    def get_nickname(self):
        nickname_input = self.browser.find_element(
            *self.NICKNAME_INPUT_SELECTOR)

        return nickname_input.get_attribute("value")

    def click_on_save_button(self):
        save_button = self.browser.find_element(
            *self.SAVE_BUTTON_SELECTOR)

        save_button.click()

    def click_on_cancel_button(self):
        save_button = self.browser.find_element(
            *self.CANCEL_BUTTON_SELECTOR)

        save_button.click()
