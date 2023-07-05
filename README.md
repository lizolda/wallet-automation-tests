# Automation tests for Wallet App

This is the project to showcase the automation tests for Wallet App.

It's written in python and uses pytest framework.

Each test has it's own file, it's readable, easy to maintain and can save a lot of time doing sanity tests and discovering regression issues.

## Installing

1. Install dependencies: `python3 -m pip install -r requirements.pip`

_NOTE: On mac you should use  `pip3` and not `python3 -m pip`. It depends on your specific machine

2. Download and install latest [geckodriver](https://github.com/mozilla/geckodriver/releases)

_NOTE: as selenium is the only dependency it's very easy to dockerize it and run in CI as well_

## Running

Execute following command from the root directory:

`python3 -m pytest`

## Arguments

`WALLET_APP_URL` - app url can be injected dynamically via environment variable

`WALLET_APP_URL=https://.. python3 -m pytest`

## Project structure

```
├── src
│   ├── credit_card_form.py
│   ├── credit_cards_list.py
│   ├── dto.py
│   ├── __init__.py
│   ├── utils.py
│   └── wallet_app.py
└── tests
    ├── conftest.py
    ...
    ├── test_add_credit_card.py
    └── test_set_credit_card_as_primary.py

```

- `src/` - directory that holds business logic of how to manipulate the application
- `src/wallet_app.py` - holds orchestrator class that proxies requests to low level implementation classes.

  For an example: `src/credit_cards_list.py`. Class that knows how to work with the list of saved credit cards. `wallet_app.py` does not hold any logic of how the list works in low level. This way list logic is encapsulated in the `CreditCardsList` class, which make this project easy to maintain and understand.

- `tests/` directory that holds all of the test cases. New tests should be added to this directory. Each test has it's own file, as it's easier to work with with small files
