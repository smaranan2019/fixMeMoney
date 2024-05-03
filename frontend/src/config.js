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
      {'id': 15838, 'type': 'expense', 'name': 'GONGYUAN MALATANG-CCP SINGAPORE', 'amount': 35.75, 'compounds': false}
      , 
      {'id': 55936, 'type': 'expense', 'name': 'Grab* A-6XDGSUEGWJ3X Singapore', 'amount': 1.88, 'compounds': false}, 
      {'id': 63520, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': false}, 
      {'id': 35117, 'type': 'expense', 'name': 'NUODLE @ CBP Singapore', 'amount': 24.8, 'compounds': false}, 
      {'id': 81854, 'type': 'expense', 'name': 'GIGA 68255000', 'amount': 18.33, 'compounds': false}, 
      {'id': 73110, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 3.5, 'compounds': false}, 
      {'id': 95757, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 1.0, 'compounds': false}, 
      {'id': 91157, 'type': 'expense', 'name': 'AMAR AND CO CAFFE PTE SINGAPORE', 'amount': 3.6, 'compounds': false}, 
      {'id': 93871, 'type': 'expense', 'name': 'BUS/MRT 400160552 SINGAPORE<br/>Ref No. : 74541834066288082730107', 'amount': 5.98, 'compounds': false}, 
      {'id': 98545, 'type': 'expense', 'name': 'MY KAMPUNG - CHANGI CITY SINGAPORE', 'amount': 6.8, 'compounds': false}, 
      {'id': 92150, 'type': 'expense', 'name': 'SINGAPOREAlR6182450658840SlNGAPORE', 'amount': 1959.2, 'compounds': false}, 
      {'id': 39820, 'type': 'expense', 'name': '7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834059288076681505', 'amount': 4.0, 'compounds': false}, 
      {'id': 75841, 'type': 'expense', 'name': 'BUS/MRT 392892886 SINGAPORE', 'amount': 1.75, 'compounds': false}, 
      {'id': 85741, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE<br/>Ref No. : 74541834061288076689827', 'amount': 11.9, 'compounds': false}, 
      {'id': 23424, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': false}, 
      {'id': 68456, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE<br/>Ref No. : 74541834064288084505194', 'amount': 2.9, 'compounds': false}, 
      {'id': 54817, 'type': 'expense', 'name': 'MUYOO BAKERY SINGAPORE', 'amount': 7.9, 'compounds': false}, {'id': 48248, 'type': 'expense', 'name': 'DON DON DONKI - NORTHPOINSINGAPORE', 'amount': 4.9, 'compounds': false}, 
      {'id': 65880, 'type': 'expense', 'name': 'THE COFFEE BEAN-CCP SINGAPORE', 'amount': 4.4, 'compounds': false}, 
      {'id': 19225, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 2.9, 'compounds': false}, 
      {'id': 99594, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': false}, 
      {'id': 42642, 'type': 'expense', 'name': '7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834062288077877644', 'amount': 4.5, 'compounds': false}, 
      {'id': 62187, 'type': 'expense', 'name': 'SPORE SPORTS HUB-NTNL STSINGAPORE', 'amount': 8.5, 'compounds': false}, 
      {'id': 56598, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE<br/>Ref No. : 74541834060288076508986', 'amount': 8.5, 'compounds': false}, 
      {'id': 66450, 'type': 'expense', 'name': 'NTIJC FairPrice App PaymenSlNGAPORE', 'amount': 1.7, 'compounds': false}, 
      {'id': 32491, 'type': 'expense', 'name': 'GV TAMPINES SINGAPORE<br/>Ref No. : 74541834058288070079947', 'amount': 13.5, 'compounds': false}, 
      {'id': 55278, 'type': 'expense', 'name': 'MEXICAN FOOD CORP SV PTE SINGAPORE<br/>Ref No. : 74777154058000004955078', 'amount': 9.0, 'compounds': false}, 
      {'id': 33813, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE', 'amount': 14.68, 'compounds': false}, 
      {'id': 86318, 'type': 'expense', 'name': 'YA KUN EASTPOINT MALL Singapore<br/>Ref No. : 74556224058102131622692', 'amount': 6.5, 'compounds': false}, {'id': 17521, 'type': 'expense', 'name': 'Grab* 3-C6EGTPAXLECXRN Singapore', 'amount': 7.9, 'compounds': false}, {'id': 15163, 'type': 'expense', 'name': 'COMPASS GROUP JPMORG SINGAPORE', 'amount': 1.7, 'compounds': false}, {'id': 88897, 'type': 'expense', 'name': 'CHICHA SAN CHEN - EASTPOISINGAPORE', 'amount': 5.6, 'compounds': false}, {'id': 62820, 'type': 'expense', 'name': 'DAISO JAPAN - CCP SINGAPORE', 'amount': 2.18, 'compounds': false}, {'id': 82526, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 7.8, 'compounds': false}, {'id': 13699, 'type': 'expense', 'name': 'Grab* A-63R42R6WWEQT Singapore<br/>Ref No. : 74777154061000108378065', 'amount': 17.4, 'compounds': false}, {'id': 54189, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 0.96, 'compounds': false}, {'id': 41551, 'type': 'expense', 'name': '7-ELEVEN-51 CBP CENTRAL 2SlNGAPORE', 'amount': 6.8, 'compounds': false}, {'id': 89450, 'type': 'expense', 'name': 'NET*VENDIT SINGAPORE<br/>Ref No. : 74541834061288077679967', 'amount': 10.0, 'compounds': false}, {'id': 64670, 'type': 'expense', 'name': 'NTIJC FairPrice App PaymenSlNGAPORE', 'amount': 20.74, 'compounds': false}, {'id': 78565, 'type': 'expense', 'name': 'BUS/MRT 396349096 SINGAPORE', 'amount': 2.29, 'compounds': false}, {'id': 64348, 'type': 'expense', 'name': 'IDATEN UDON - CHANGI CITYSINGAPORE', 'amount': 10.2, 'compounds': false}, {'id': 75860, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE<br/>Ref No. : 74541834069288081757116', 'amount': 16.99, 'compounds': false}, {'id': 97715, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 3.5, 'compounds': false}, {'id': 99364, 'type': 'expense', 'name': 'NTIJC FairPrice App PaymenSlNGAPORE', 'amount': 4.03, 'compounds': false}, {'id': 21597, 'type': 'expense', 'name': 'NTUC FairPrice App PaymenSlNGAPORE<br/>Ref No. : 74777154063000603063087', 'amount': 72.58, 'compounds': false}, {'id': 54645, 'type': 'expense', 'name': 'CHICHA SAN CHEN - WATERWASINGAPORE<br/>Ref No. : 74508984061017064944892', 'amount': 23.0, 'compounds': false}, 
      {'id': 49165, 'type': 'expense', 'name': 'NTUC FairPrice App PaymenSlNGAPORE', 'amount': 23.23, 'compounds': false}, 
      {'id': 42139, 'type': 'expense', 'name': 'GIANT-SIMEI MRT SINGAPORE<br/>Ref No. : 74541834059288071971489', 'amount': 2.75, 'compounds': false}, 
      {'id': 51774, 'type': 'expense', 'name': 'AMAR AND CO CAFFE PTE SINGAPORE', 'amount': 6.8, 'compounds': false}, 
      {'id': 28794, 'type': 'expense', 'name': 'BUS/MRT 400545157 SINGAPORE', 'amount': 1.09, 'compounds': false},
      {'id': 89890, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 2.9, 'compounds': false}, 
      {'id': 34670, 'type': 'expense', 'name': '7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834062288077878329', 'amount': 1.0, 'compounds': false}, 
      {'id': 41263, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 1.5, 'compounds': false}, 
      {'id': 88256, 'type': 'expense', 'name': 'ANDES CHANG QLUB, SG SINGAPORE', 'amount': 18.9, 'compounds': false}, 
      {'id': 85582, 'type': 'expense', 'name': 'TAKAGI RAMEN-SIMEI SINGAPORE<br/>Ref No. : 74103804059000004330672', 'amount': 11.5, 'compounds': false}, 
      {'id': 55561, 'type': 'expense', 'name': 'UOB ONE CASH REBATE BILL REDEMPTION', 'amount': 200.0, 'compounds': false}, 
      {'id': 23572, 'type': 'expense', 'name': '7-ELEVEN-ORCHARD MRT SINGAPORE', 'amount': 2.4, 'compounds': false}, 
      {'id': 99648, 'type': 'expense', 'name': 'PAYMT THRU E-BANK/HOMEB/CYBERB (EP38)', 'amount': 4696.22, 'compounds': false}, 
      {'id': 52318, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE', 'amount': 10.98, 'compounds': false}, 
      {'id': 88652, 'type': 'expense', 'name': 'insta360 camera', 'amount': 850.42, 'compounds': false}, 
      {'id': 66829, 'type': 'expense', 'name': 'SUBWAY - KALLANGWAVE MALLSINGAPORE<br/>Ref No. : 74508984061017066775245', 'amount': 4.0, 'compounds': false}, 
      {'id': 47165, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 1.0, 'compounds': false}, 
      {'id': 97858, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 2.9, 'compounds': false}, 
      {'id': 59325, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 3.0, 'compounds': false}, 
      {'id': 46870, 'type': 'expense', 'name': 'LLAO LLAO - CCP SINGAPORE', 'amount': 8.0, 'compounds': false}, 
      {'id': 13315, 'type': 'expense', 'name': 'PRIME SUPERMARKET Singapore', 'amount': 14.9, 'compounds': false}, 
      {'id': 57898, 'type': 'expense', 'name': 'GIGA 68255000', 'amount': 18.33, 'compounds': false}, 
      {'id': 71344, 'type': 'expense', 'name': 'Grab* A-6XDGF7DGWJ3X Singapore', 'amount': 34.8, 'compounds': false}, 
      {'id': 49357, 'type': 'expense', 'name': 'ONE CARD ADDITIONAL REBATE', 'amount': 82.38, 'compounds': false}, 
      {'id': 61120, 'type': 'expense', 'name': 'LLAO LLAO - CCP SINGAPORE<br/>Ref No. : 74541834064288086831333', 'amount': 8.9, 'compounds': false}, 
      {'id': 59658, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': false}, 
      {'id': 43194, 'type': 'expense', 'name': 'WTROLD-TEA-HUT-CHANGI 6586988741', 'amount': 3.0, 'compounds': false}, 
      {'id': 61555, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE', 'amount': 15.36, 'compounds': false}, 
      {'id': 35534, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 2.9, 'compounds': false}
    ]
  },
};

export default CONFIG;
