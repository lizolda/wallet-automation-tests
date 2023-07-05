from src.wallet_app import WalletApp
from dateutil.relativedelta import relativedelta
from datetime import date
from src.dto import CreditCardInfo
from src import utils


def test_add_valid_credit_card(browser, url):
    """
        Test steps:
         - Fill in the form with valid credit card info
         - Check the form state equals to what has been entered
         - Click on save button
         - Check we now have one card saved
         - Compare card attributes with initial card data
    """
   
    future_date = date.today() + relativedelta(months=3)

    wallet_app = WalletApp(browser, url)


    wallet_app.load()

    expected_card_info = CreditCardInfo(
        credit_card_number="1111222233334444",
        expiration=utils.get_expiration_from_date_to_input_string(future_date),
        street_address="mock street",
        city="New york",
        state="Alaska",
        postal_code=1234,
        nickname=""
    )

    wallet_app.fill_form(
        form_data=expected_card_info,
    )

    actual_data = wallet_app.get_form_state()

    assert actual_data == expected_card_info, "expected form to have correct card data"

    wallet_app.save_form()

    all_credit_cards = wallet_app.get_all_credit_cards()

    assert len(all_credit_cards) == 1, "expected to have one credit card saved"

    actual_saved_credit_card = all_credit_cards[0]

    assert actual_saved_credit_card.nickname == expected_card_info.nickname

    assert actual_saved_credit_card.expiration == expected_card_info.expiration.replace(
        " ", ""), "expected saved expiration to match input expiration"

    assert actual_saved_credit_card.street_address == expected_card_info.street_address, "expected saved street address to match input street address"

    assert actual_saved_credit_card.city == expected_card_info.city, "expected saved city to match input city"

    assert actual_saved_credit_card.state == expected_card_info.state, "expected saved state to match input state in address"

    assert actual_saved_credit_card.credit_card_number == expected_card_info.credit_card_number[
        -4:], "expected saved credit card number to match input credit card number"
