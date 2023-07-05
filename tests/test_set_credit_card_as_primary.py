from src.wallet_app import WalletApp
from dateutil.relativedelta import relativedelta
from datetime import date
from src.dto import CreditCardInfo
from src import utils


def test_set_credit_card_as_primary(browser, url):
    """
        Test steps:
         - Fill in the form with two valid credit cards
         - Check we now have two cards saved
         - Compare card attributes with initial card data
         - Choose first saved card to be primary and click on Set as Primary
         - Check same card is now has 'Primary' badge
    """

    first_future_date = date.today() + relativedelta(months=2)
    second_future_date = date.today() + relativedelta(months=4)

    wallet_app = WalletApp(browser, url)

    wallet_app.load()

    first_card = CreditCardInfo(
        credit_card_number="1234123412341234",
        expiration=utils.get_expiration_from_date_to_input_string(
            first_future_date),
        street_address="not real street",
        city="Dallas",
        state="Texas",
        postal_code=321,
        nickname="My first card"
    )

    second_card = CreditCardInfo(
        credit_card_number="4321432143214321",
        expiration=utils.get_expiration_from_date_to_input_string(
            second_future_date),
        street_address="not real street 2",
        city="Alford",
        state="Florida",
        postal_code=321,
        nickname="My second card"
    )

    wallet_app.fill_form(
        form_data=first_card,
    )

    actual_first_card_data = wallet_app.get_form_state()

    assert actual_first_card_data == first_card, "form contains wrong data for first card"

    wallet_app.save_form()

    all_credit_cards = wallet_app.get_all_credit_cards()

    assert len(all_credit_cards) == 1, "expected to have one credit card saved"

    wallet_app.click_on_add_credit_card()

    wallet_app.fill_form(
        form_data=second_card,
    )

    actual_second_card_data = wallet_app.get_form_state()

    assert actual_second_card_data == second_card, "form contains wrong data for second card"

    wallet_app.save_form()

    all_credit_cards = wallet_app.get_all_credit_cards()

    assert len(all_credit_cards) == 2, "expected to have 2 credit cards saved"

    card_to_set_as_primary = all_credit_cards[1]

    assert card_to_set_as_primary.is_primary == False, "expected target credit card to not be primary initially"

    wallet_app.set_credit_card_as_primary_by_four_digits(
        card_to_set_as_primary.credit_card_number
    )

    all_credit_cards = wallet_app.get_all_credit_cards()

    updated_card = None
    for card in all_credit_cards:

        if card.credit_card_number == card_to_set_as_primary.credit_card_number:
            updated_card = card
            break

    assert updated_card != None, "expected to found card with the same card number after setting it as primary"

    assert updated_card.is_primary == True, "expected updated credit card to be primary"
