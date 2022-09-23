## peerberryapi

The peerberryapi package is a Python API wrapper for the Peerberry platform.
Peerberry currently has no API documentation and some endpoints could be simplified/optimized, which is one of the main goals of this project.

Peerberry platform: https://peerberry.com/

## Requirements 

Python 3.7+

Main dependencies:
  <ul>
    <li>pandas for the large data handling.</li>
    <li>pyotp for handling two-factor authentication.</li>
    <li>requests for handling HTTP requests to the Peerberry API.</li>
    <li>openpyxl for parsing spreadsheets supplied by Peerberry.</li>
  </ul>

## Installation

```bash
pip install peerberryapi
```

## Usage

```python
from peerberryapi import API


# Authenticate to the API client (You won't need to manually authenticate again after this)
api_client = API(
  email='YOUR EMAIL HERE',
  password='YOUR PASSWORD HERE',
  tfa_secret='YOUR BASE32 TFA SECRET HERE',  # This is only required if you have two-factor authentication enabled on your account
)

# Gets investor profile data
print(api_client.get_profile())
```

<pre>
API functions:

Investor/portfolio data functions:
  get_profile -> Gets investor profile.
  get_loyalty_tier -> Gets loyalty tier, tier requirements, and the tier's benefits.
  get_overview -> Gets portfolio overview (Balance, total invested, total profit, net annual return, etc.).
  get_profit_overview -> Gets portfolio's profit on a daily, monthly or yearly basis (Data used in your profile's profit chart).
  get_investment_status -> Gets percentage of funds in different investment statuses (Current, late by 1-15 days, 16-30 days, and 31-60 days).
 
Marketplace/loan data functions:
  get_loans -> Gets loans available for investment in the Peerberry marketplace according to the filters you specify.
  get_loan_details -> Gets available information about the loan, the borrower, and the loan's payments schedule.
  purchase_loan -> Invests in a loan with the amount you specify.

Investment data functions:
  get_investments -> Gets current or finished investments in accordance to the filters you specify (It's recommended to use the get_mass_investments function when fetching more than ~350 investments at once).
  get_mass_investments -> Gets current or finished investments either as an Excel or as a Pandas DataFrame in accordance with the filters you specify (It's recommended to use this function when fetching more than ~350 investments at once).
  get_account_summary -> Gets account's transaction summary (Invested funds, principal payments, interest payments, deposits, etc.).

Transaction data functions:
  get_transactions -> Gets transactions as a Pandas DataFrame in accordance with the filters you specify.
  get_mass_transactions -> Gets transactions either as an Excel or as a Pandas DataFrame.
  
Authentication functions:
  logout -> Logs out of Peerberry and revokes your access token. Recommended to use after you finish all your operations.
</pre>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
