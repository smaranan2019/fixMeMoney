const CONFIG = {
  MILISECONDS_IN_YEAR: 1000 * 60 * 60 * 24 * 365,
  REFRESH_INTERVAL: 100,
  INCOME_ESTIMATE_APR: 7,
  LOCALSTORAGE_KEY: 'personal_finance_items',
  ITEM_TYPE: {
    ASSET: 'asset',
    LIABILITY: 'liability',
    INCOME: 'income',
    EXPENSE: 'expense',
  },
  ocr_api : "http://localhost:5200/ocr",
  SAMPLE_DATA: {
    ASSETS: [
      {
        id: 47433,
        type: 'asset',
        name: 'Bank deposit',
        amount: 10000,
        apr: 4,
        compounds: true,
      }
    ],
    LIABILITIES: [
      {
        id: 23453,
        type: 'liability',
        name: 'Student Loan',
        amount: 44000,
        apr: 4,
      }
    ],
    INCOME: [
      {
        "id": 23780,
        "type": "income",
        "name": "salary",
        "amount": 5000,
        "compounds": false
      },
      {
        "id": 23789,
        "type": "income",
        "name": "ONE CARD ENHANCED REBATE",
        "amount": 61.78,
        "compounds": false
      },
      {
        "id": 95123,
        "type": "income",
        "name": "ONE CARD ADDITIONAL REBATE",
        "amount": 82.38,
        "compounds": false
      },
      {
        "id": 48201,
        "type": "income",
        "name": "PAYMT THRU E-BANK/HOMEB/CYBERB (EP38)",
        "amount": 4696.22,
        "compounds": false
      },
      {
        "id": 71934,
        "type": "income",
        "name": "PAYMT THRU E-BANWHOMEB/CYBERB (EP04)",
        "amount": 146,
        "compounds": false
      },
      {
        "id": 10562,
        "type": "income",
        "name": "UOB ONE CASH REBATE BILL REDEMPTION",
        "amount": 200,
        "compounds": false
      }
    ],
    EXPENSES: [
      {
        "id": 98234,
        "type": "expense",
        "name": "NTIJC FairPrice App Payment",
        "amount": 18.33,
        "compounds": false
      },
      {
        "id": 74523,
        "type": "expense",
        "name": "7-ELEVEN",
        "amount": 4.03,
        "compounds": false
      },
      {
        "id": 23457,
        "type": "expense",
        "name": "Grab",
        "amount": 0.96,
        "compounds": false
      },
      {
        "id": 87321,
        "type": "expense",
        "name": "Grab",
        "amount": 34.8,
        "compounds": false
      },
      {
        "id": 12984,
        "type": "expense",
        "name": "Prime Supermarket",
        "amount": 1.88,
        "compounds": false
      },
      {
        "id": 62357,
        "type": "expense",
        "name": "NTIJC FairPrice App Payment",
        "amount": 20.74,
        "compounds": false
      },
      {
        "id": 58723,
        "type": "expense",
        "name": "NTIJC FairPrice App Payment",
        "amount": 14.9,
        "compounds": false
      },
      {
        "id": 95142,
        "type": "expense",
        "name": "Grab",
        "amount": 2.9,
        "compounds": false
      },
      {
        "id": 71234,
        "type": "expense",
        "name": "Subscription (GIGA)",
        "amount": 200,
        "compounds": false
      }
    ],
  },
};

export default CONFIG;
