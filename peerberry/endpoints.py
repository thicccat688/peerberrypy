class ENDPOINTS:
    BASE_URI = 'https://api.peerberry.com'

    LOGIN_URI = f'{BASE_URI}/v1/investor/login'
    TFA_URI = f'{BASE_URI}/v1/investor/login/2fa'

    OVERVIEW_URI = f'{BASE_URI}/v1/investor/overview'
    PROFIT_OVERVIEW_URI = f'{BASE_URI}/v1/investor/overview/profit'

    LOYALTY_URI = f'{BASE_URI}/v1/investor/loyalty'
    INVESTMENTS_STATUS_URI = f'{BASE_URI}/v2/investor/overview/investment_statuses/current'

    PROFILE_URI = f'{BASE_URI}/v1/investor/profile'
    INVESTMENTS_URI = f'{BASE_URI}/v1/investor/investments'

    LOANS_URI = f'{BASE_URI}/v1/loans'

    CASH_FLOW_URI = f'{BASE_URI}/v2/investor/transactions'
    ACCOUNT_SUMMARY_URI = f'{BASE_URI}/v2/investor/account-summary'
