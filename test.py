
import random
test_data = [
    {
        "amount": 35.75,
        "category": "food",
        "desc": "GONGYUAN MALATANG-CCP SINGAPORE",
        "id": "004ed3d4-a497-4684-b75b-fa630bf2e8ec",
        "transDate": "Fri, 08 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.88,
        "category": "transport",
        "desc": "Grab* A-6XDGSUEGWJ3X Singapore",
        "id": "0bd1b9d9-b68c-4b92-956b-161efd3167b5",
        "transDate": "Sun, 11 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "transport",
        "desc": "Grab* A-6XUFG4WWWFXF Singapore",
        "id": "0d349cbd-3021-4c3c-8960-56820d7cfd75",
        "transDate": "Fri, 16 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 24.8,
        "category": "food",
        "desc": "NUODLE @ CBP Singapore",
        "id": "0e67e665-1d91-45b7-8fbc-c6195b5dce84",
        "transDate": "Tue, 05 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 18.33,
        "category": "subscriptions",
        "desc": "GIGA 68255000",
        "id": "0f1a8772-95be-4d62-94bb-b9a331f771ff",
        "transDate": "Sat, 10 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 3.5,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "0fe505a7-f64f-445e-9c1a-b37e1b775901",
        "transDate": "Fri, 08 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.0,
        "category": "food",
        "desc": "7-ELEVEN-SIMEI MRT SINGAPORE",
        "id": "10790eba-8e66-4551-b5ac-b4f73b9a4250",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 3.6,
        "category": "food",
        "desc": "AMAR AND CO CAFFE PTE SINGAPORE",
        "id": "1297f6ba-45e1-45fe-b135-a3e9681b3d6d",
        "transDate": "Mon, 11 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 5.98,
        "category": "transport",
        "desc": "BUS/MRT 400160552 SINGAPORE<br/>Ref No. : 74541834066288082730107",
        "id": "1e336ec1-ad26-48b4-992e-2bb6731bc1ed",
        "transDate": "Sun, 03 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 6.8,
        "category": "food",
        "desc": "MY KAMPUNG - CHANGI CITY SINGAPORE",
        "id": "1eed5db9-f95e-4eaa-ad9d-58cd7bcbd3be",
        "transDate": "Sat, 24 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1959.2,
        "category": "travel",
        "desc": "SINGAPOREAlR6182450658840SlNGAPORE",
        "id": "1fbaf574-6936-4762-b926-cf76a26a19cf",
        "transDate": "Mon, 26 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4.0,
        "category": "food",
        "desc": "7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834059288076681505",
        "id": "2201dc0d-3722-4832-b1e6-c445b2dab0a7",
        "transDate": "Wed, 28 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.75,
        "category": "transport",
        "desc": "BUS/MRT 392892886 SINGAPORE",
        "id": "220a6cc6-4103-48b8-a542-f83709f9e572",
        "transDate": "Tue, 20 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 11.9,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE<br/>Ref No. : 74541834061288076689827",
        "id": "22e341e2-22ac-49e3-9668-6a3ca8416638",
        "transDate": "Fri, 01 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "transport",
        "desc": "Grab* A-6XUFG4WWWFXF Singapore",
        "id": "2a7ebcb6-0644-4568-8fbb-2b68a5970af1",
        "transDate": "Sat, 17 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "food",
        "desc": "7-ELEVEN-SIMEI MRT SINGAPORE<br/>Ref No. : 74541834064288084505194",
        "id": "31354fb9-76f9-4139-b4c9-a10bbc92fefd",
        "transDate": "Sun, 03 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 7.9,
        "category": "food",
        "desc": "MUYOO BAKERY SINGAPORE",
        "id": "32f22a4c-8eec-4574-a46d-c09b72ec8b98",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4.9,
        "category": "food",
        "desc": "DON DON DONKI - NORTHPOINSINGAPORE",
        "id": "349e117e-3ee6-4517-ae06-3ad985f5719c",
        "transDate": "Sun, 18 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4.4,
        "category": "food",
        "desc": "THE COFFEE BEAN-CCP SINGAPORE",
        "id": "3593a2b4-6458-4be5-92c9-e3baa0f2ea6d",
        "transDate": "Fri, 08 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "food",
        "desc": "7-ELEVEN-SIMEI MRT SINGAPORE",
        "id": "37fc8ab8-ab67-44e1-90ec-fe7a2033d608",
        "transDate": "Sun, 18 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "transport",
        "desc": "Grab* A-6XUFG4WWWFXF Singapore",
        "id": "451bed70-75c1-41fa-8436-65689597e0b7",
        "transDate": "Wed, 14 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4.5,
        "category": "food",
        "desc": "7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834062288077877644",
        "id": "482e1b56-86e0-41fb-baac-d1962c7f739c",
        "transDate": "Sat, 02 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 8.5,
        "category": "food",
        "desc": "SPORE SPORTS HUB-NTNL STSINGAPORE",
        "id": "4a93e23c-612c-4680-88f6-87fd92f6584b",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 8.5,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE<br/>Ref No. : 74541834060288076508986",
        "id": "4ac9ea8c-dfcb-466a-a781-5a3b62250e96",
        "transDate": "Thu, 29 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.7,
        "category": "subscriptions",
        "desc": "NTIJC FairPrice App PaymenSlNGAPORE",
        "id": "4c238df8-b5c2-433a-8f4e-bce0ad5baeec",
        "transDate": "Wed, 06 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 13.5,
        "category": "others",
        "desc": "GV TAMPINES SINGAPORE<br/>Ref No. : 74541834058288070079947",
        "id": "4e11c717-2429-4eab-9753-677bc43040e6",
        "transDate": "Tue, 27 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 9.0,
        "category": "food",
        "desc": "MEXICAN FOOD CORP SV PTE SINGAPORE<br/>Ref No. : 74777154058000004955078",
        "id": "4f602c04-70f9-4ada-a4e3-bfad7a81de8e",
        "transDate": "Tue, 27 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 14.68,
        "category": "others",
        "desc": "SHOPEE SINGAPORE MP SINGAPORE",
        "id": "51119354-767c-494c-93c5-a39d2e8d3c7c",
        "transDate": "Thu, 29 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 6.5,
        "category": "food",
        "desc": "YA KUN EASTPOINT MALL Singapore<br/>Ref No. : 74556224058102131622692",
        "id": "547fbc38-b91b-4cf1-ab46-31486de373d0",
        "transDate": "Tue, 27 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 7.9,
        "category": "transport",
        "desc": "Grab* 3-C6EGTPAXLECXRN Singapore",
        "id": "570b273d-1a59-4b2e-9be1-2e0d9b71feaf",
        "transDate": "Fri, 23 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.7,
        "category": "subscriptions",
        "desc": "COMPASS GROUP JPMORG SINGAPORE",
        "id": "5a550e06-9f76-4af3-9978-206e484bd437",
        "transDate": "Sat, 24 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 5.6,
        "category": "food",
        "desc": "CHICHA SAN CHEN - EASTPOISINGAPORE",
        "id": "5c5d9974-ed46-4b18-87fe-e8e2a51be4cf",
        "transDate": "Tue, 27 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.18,
        "category": "others",
        "desc": "DAISO JAPAN - CCP SINGAPORE",
        "id": "5d2e47f9-ace3-4045-9ffa-e34d664edd63",
        "transDate": "Fri, 08 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 7.8,
        "category": "food",
        "desc": "7-ELEVEN-SIMEI MRT SINGAPORE",
        "id": "5ed9e4f0-a3fb-4a79-8c80-8ed67e2a4c73",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 17.4,
        "category": "transport",
        "desc": "Grab* A-63R42R6WWEQT Singapore<br/>Ref No. : 74777154061000108378065",
        "id": "6534f6c1-caf0-4af8-9530-f49e0fe00a23",
        "transDate": "Fri, 01 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 0.96,
        "category": "groceries",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "674ce90f-403f-41aa-924f-0c10df69b711",
        "transDate": "Sat, 10 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 6.8,
        "category": "food",
        "desc": "7-ELEVEN-51 CBP CENTRAL 2SlNGAPORE",
        "id": "681d6303-5839-4782-aa25-ad619adf0317",
        "transDate": "Thu, 07 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 10.0,
        "category": "food",
        "desc": "NET*VENDIT SINGAPORE<br/>Ref No. : 74541834061288077679967",
        "id": "69a0b8ac-335e-48b2-90d4-49e279f13761",
        "transDate": "Fri, 01 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 20.74,
        "category": "groceries",
        "desc": "NTIJC FairPrice App PaymenSlNGAPORE",
        "id": "781fb74f-e478-4e69-baa1-85067f632589",
        "transDate": "Sun, 11 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.29,
        "category": "transport",
        "desc": "BUS/MRT 396349096 SINGAPORE",
        "id": "7b5b8aab-ebbc-4c4d-905b-70e4788c1204",
        "transDate": "Mon, 26 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 10.2,
        "category": "food",
        "desc": "IDATEN UDON - CHANGI CITYSINGAPORE",
        "id": "8bb09f02-a08c-4120-9964-c39182fceadf",
        "transDate": "Mon, 04 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 16.99,
        "category": "apparel",
        "desc": "SHOPEE SINGAPORE MP SINGAPORE<br/>Ref No. : 74541834069288081757116",
        "id": "8c92dd20-30b9-48c4-8a23-271e2c30680d",
        "transDate": "Sat, 02 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 3.5,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "8d79b1ee-f19a-413d-9915-090095b2e77f",
        "transDate": "Tue, 05 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4.03,
        "category": "groceries",
        "desc": "NTIJC FairPrice App PaymenSlNGAPORE",
        "id": "98730ebd-18e4-492e-a580-e3a5cbc82bd1",
        "transDate": "Sat, 10 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 72.58,
        "category": "food",
        "desc": "NTUC FairPrice App PaymenSlNGAPORE<br/>Ref No. : 74777154063000603063087",
        "id": "9a37a11c-82fc-4339-8455-2771ab80badc",
        "transDate": "Sun, 03 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 23.0,
        "category": "food",
        "desc": "CHICHA SAN CHEN - WATERWASINGAPORE<br/>Ref No. : 74508984061017064944892",
        "id": "a06b8bc3-448a-46e3-acd8-11e9fd1513d7",
        "transDate": "Fri, 01 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 23.23,
        "category": "food",
        "desc": "NTUC FairPrice App PaymenSlNGAPORE",
        "id": "a2ba129b-f66e-4e12-84aa-5bab6d10a269",
        "transDate": "Mon, 26 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.75,
        "category": "food",
        "desc": "GIANT-SIMEI MRT SINGAPORE<br/>Ref No. : 74541834059288071971489",
        "id": "a397342b-5d75-4cb8-99c7-373402ec3302",
        "transDate": "Wed, 28 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 6.8,
        "category": "food",
        "desc": "AMAR AND CO CAFFE PTE SINGAPORE",
        "id": "a3bad21f-856f-4f89-9ee1-d8eeb5b0aacf",
        "transDate": "Mon, 26 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.09,
        "category": "transport",
        "desc": "BUS/MRT 400545157 SINGAPORE",
        "id": "a4f1a8da-8eb6-4f6b-a642-19fa22d322c0",
        "transDate": "Mon, 04 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "a91cfba8-e83b-4ba0-a00c-22ea79b07fd2",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.0,
        "category": "food",
        "desc": "7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834062288077878329",
        "id": "b2624ba1-1101-42cb-9843-517108da295f",
        "transDate": "Sat, 02 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.5,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "b3a0d8be-fd65-4a8e-bd8c-37b19d008cf4",
        "transDate": "Thu, 07 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 18.9,
        "category": "food",
        "desc": "ANDES CHANG QLUB, SG SINGAPORE",
        "id": "b4eb1b7d-8326-4218-8473-0f6047f228b1",
        "transDate": "Thu, 07 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 11.5,
        "category": "food",
        "desc": "TAKAGI RAMEN-SIMEI SINGAPORE<br/>Ref No. : 74103804059000004330672",
        "id": "b7864ced-3b81-40b5-92f1-2ac1917ed477",
        "transDate": "Wed, 28 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 200.0,
        "category": "others",
        "desc": "UOB ONE CASH REBATE BILL REDEMPTION",
        "id": "b825187c-5277-4156-8a35-3f3dc84b069e",
        "transDate": "Fri, 09 Feb 2024 00:00:00 GMT",
        "type": "credit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.4,
        "category": "food",
        "desc": "7-ELEVEN-ORCHARD MRT SINGAPORE",
        "id": "b8453953-bf36-440f-82c0-5ff3a8754c49",
        "transDate": "Sat, 17 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4696.22,
        "category": "others",
        "desc": "PAYMT THRU E-BANK/HOMEB/CYBERB (EP38)",
        "id": "ba3edc9b-cbfd-4568-b652-2baedc95a19c",
        "transDate": "Fri, 23 Feb 2024 00:00:00 GMT",
        "type": "credit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 10.98,
        "category": "others",
        "desc": "SHOPEE SINGAPORE MP SINGAPORE",
        "id": "c0dc97b0-6aa8-485d-8e40-33cc0fbd29f6",
        "transDate": "Sun, 18 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 850.42,
        "category": "apparel",
        "desc": "insta360 camera",
        "id": "c1b8e2e4-f30c-436b-99be-cbeb99553f77",
        "transDate": "Tue, 05 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 4.0,
        "category": "food",
        "desc": "SUBWAY - KALLANGWAVE MALLSINGAPORE<br/>Ref No. : 74508984061017066775245",
        "id": "c253d926-83df-447c-8cdf-0d27b3e13ad7",
        "transDate": "Fri, 01 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 1.0,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "c3414624-821e-45b1-be28-2be6fea91620",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "food",
        "desc": "7-ELEVEN-SIMEI MRT SINGAPORE",
        "id": "c51f6dcb-71bf-43c3-90f9-c7a5e6eb4c00",
        "transDate": "Fri, 23 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 3.0,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "c5775da0-78dd-4513-82ea-22fd27664a38",
        "transDate": "Wed, 21 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 8.0,
        "category": "food",
        "desc": "LLAO LLAO - CCP SINGAPORE",
        "id": "cea014d3-dc77-490a-bb12-4ce114633aff",
        "transDate": "Thu, 07 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 14.9,
        "category": "groceries",
        "desc": "PRIME SUPERMARKET Singapore",
        "id": "d23442ee-5f23-4910-9820-fb4ce72ef0b2",
        "transDate": "Tue, 12 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 18.33,
        "category": "bills",
        "desc": "GIGA 68255000",
        "id": "d6b66883-56dc-4ee0-a85f-647a09252222",
        "transDate": "Sat, 09 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 34.8,
        "category": "transport",
        "desc": "Grab* A-6XDGF7DGWJ3X Singapore",
        "id": "d72e5b67-d018-4e60-97d9-ae154d09c19a",
        "transDate": "Sun, 11 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 82.38,
        "category": "others",
        "desc": "ONE CARD ADDITIONAL REBATE",
        "id": "d983335c-2e45-4ac3-bea8-bbd51c5f6e09",
        "transDate": "Tue, 12 Mar 2024 00:00:00 GMT",
        "type": "credit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 8.9,
        "category": "food",
        "desc": "LLAO LLAO - CCP SINGAPORE<br/>Ref No. : 74541834064288086831333",
        "id": "e13ce891-e29d-4444-aa39-2561571ac036",
        "transDate": "Mon, 04 Mar 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "transport",
        "desc": "Grab* A-6XUFG4WWWFXF Singapore",
        "id": "e76abc75-f905-460b-9485-43be18809007",
        "transDate": "Thu, 15 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 3.0,
        "category": "food",
        "desc": "WTROLD-TEA-HUT-CHANGI 6586988741",
        "id": "e8c3680a-d2f2-4ede-8d58-42d660a65661",
        "transDate": "Wed, 21 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 15.36,
        "category": "others",
        "desc": "SHOPEE SINGAPORE MP SINGAPORE",
        "id": "f5a565aa-45ab-4d1a-8409-d0e3049faf68",
        "transDate": "Mon, 26 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    },
    {
        "amount": 2.9,
        "category": "food",
        "desc": "7-ELEVEN-CHANGI CITY PT SINGAPORE",
        "id": "fba018fd-cf12-4385-b1e7-a4d42b1ba47e",
        "transDate": "Mon, 26 Feb 2024 00:00:00 GMT",
        "type": "debit",
        "userConfirm": True,
        "userId": 1
    }
]

output = []
for i in test_data:
    output_item = {}
    output_item["id"] = int(''.join(str(random.randint(1, 9)) for _ in range(4)) + str(random.randint(0, 9)))
    output_item["type"] = "expense"
    output_item["name"] = i["desc"]
    output_item["amount"] = i["amount"]
    output_item["compounds"] = False

    output.append(output_item)

print(output)


test_new = [{'id': 15838, 'type': 'expense', 'name': 'GONGYUAN MALATANG-CCP SINGAPORE', 'amount': 35.75, 'compounds': 'false'}, {'id': 55936, 'type': 'expense', 'name': 'Grab* A-6XDGSUEGWJ3X Singapore', 'amount': 1.88, 'compounds': 'false'}, {'id': 63520, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': 'false'}, {'id': 35117, 'type': 'expense', 'name': 'NUODLE @ CBP Singapore', 'amount': 24.8, 'compounds': 'false'}, {'id': 81854, 'type': 'expense', 'name': 'GIGA 68255000', 'amount': 18.33, 'compounds': 'false'}, {'id': 73110, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 3.5, 'compounds': 'false'}, {'id': 95757, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 1.0, 'compounds': 'false'}, {'id': 91157, 'type': 'expense', 'name': 'AMAR AND CO CAFFE PTE SINGAPORE', 'amount': 3.6, 'compounds': 'false'}, {'id': 93871, 'type': 'expense', 'name': 'BUS/MRT 400160552 SINGAPORE<br/>Ref No. : 74541834066288082730107', 'amount': 5.98, 'compounds': 'false'}, {'id': 98545, 'type': 'expense', 'name': 'MY KAMPUNG - CHANGI CITY SINGAPORE', 'amount': 6.8, 'compounds': 'false'}, {'id': 92150, 'type': 'expense', 'name': 'SINGAPOREAlR6182450658840SlNGAPORE', 'amount': 1959.2, 'compounds': 'false'}, {'id': 39820, 'type': 'expense', 'name': '7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834059288076681505', 'amount': 4.0, 'compounds': 'false'}, {'id': 75841, 'type': 'expense', 'name': 'BUS/MRT 392892886 SINGAPORE', 'amount': 1.75, 'compounds': 'false'}, {'id': 85741, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE<br/>Ref No. : 74541834061288076689827', 'amount': 11.9, 'compounds': 'false'}, {'id': 23424, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': 'false'}, {'id': 68456, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE<br/>Ref No. : 74541834064288084505194', 'amount': 2.9, 'compounds': 'false'}, {'id': 54817, 'type': 'expense', 'name': 'MUYOO BAKERY SINGAPORE', 'amount': 7.9, 'compounds': 'false'}, {'id': 48248, 'type': 'expense', 'name': 'DON DON DONKI - NORTHPOINSINGAPORE', 'amount': 4.9, 'compounds': 'false'}, {'id': 65880, 'type': 'expense', 'name': 'THE COFFEE BEAN-CCP SINGAPORE', 'amount': 4.4, 'compounds': 'false'}, {'id': 19225, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 2.9, 'compounds': 'false'}, {'id': 99594, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': 'false'}, {'id': 42642, 'type': 'expense', 'name': '7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834062288077877644', 'amount': 4.5, 'compounds': 'false'}, {'id': 62187, 'type': 'expense', 'name': 'SPORE SPORTS HUB-NTNL STSINGAPORE', 'amount': 8.5, 'compounds': 'false'}, {'id': 56598, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE<br/>Ref No. : 74541834060288076508986', 'amount': 8.5, 'compounds': 'false'}, {'id': 66450, 'type': 'expense', 'name': 'NTIJC FairPrice App PaymenSlNGAPORE', 'amount': 1.7, 'compounds': 'false'}, {'id': 32491, 'type': 'expense', 'name': 'GV TAMPINES SINGAPORE<br/>Ref No. : 74541834058288070079947', 'amount': 13.5, 'compounds': 'false'}, {'id': 55278, 'type': 'expense', 'name': 'MEXICAN FOOD CORP SV PTE SINGAPORE<br/>Ref No. : 74777154058000004955078', 'amount': 9.0, 'compounds': 'false'}, {'id': 33813, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE', 'amount': 14.68, 'compounds': 'false'}, {'id': 86318, 'type': 'expense', 'name': 'YA KUN EASTPOINT MALL Singapore<br/>Ref No. : 74556224058102131622692', 'amount': 6.5, 'compounds': 'false'}, {'id': 17521, 'type': 'expense', 'name': 'Grab* 3-C6EGTPAXLECXRN Singapore', 'amount': 7.9, 'compounds': 'false'}, {'id': 15163, 'type': 'expense', 'name': 'COMPASS GROUP JPMORG SINGAPORE', 'amount': 1.7, 'compounds': 'false'}, {'id': 88897, 'type': 'expense', 'name': 'CHICHA SAN CHEN - EASTPOISINGAPORE', 'amount': 5.6, 'compounds': 'false'}, {'id': 62820, 'type': 'expense', 'name': 'DAISO JAPAN - CCP SINGAPORE', 'amount': 2.18, 'compounds': 'false'}, {'id': 82526, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 7.8, 'compounds': 'false'}, {'id': 13699, 'type': 'expense', 'name': 'Grab* A-63R42R6WWEQT Singapore<br/>Ref No. : 74777154061000108378065', 'amount': 17.4, 'compounds': 'false'}, {'id': 54189, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 0.96, 'compounds': 'false'}, {'id': 41551, 'type': 'expense', 'name': '7-ELEVEN-51 CBP CENTRAL 2SlNGAPORE', 'amount': 6.8, 'compounds': 'false'}, {'id': 89450, 'type': 'expense', 'name': 'NET*VENDIT SINGAPORE<br/>Ref No. : 74541834061288077679967', 'amount': 10.0, 'compounds': 'false'}, {'id': 64670, 'type': 'expense', 'name': 'NTIJC FairPrice App PaymenSlNGAPORE', 'amount': 20.74, 'compounds': 'false'}, {'id': 78565, 'type': 'expense', 'name': 'BUS/MRT 396349096 SINGAPORE', 'amount': 2.29, 'compounds': 'false'}, {'id': 64348, 'type': 'expense', 'name': 'IDATEN UDON - CHANGI CITYSINGAPORE', 'amount': 10.2, 'compounds': 'false'}, {'id': 75860, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE<br/>Ref No. : 74541834069288081757116', 'amount': 16.99, 'compounds': 'false'}, {'id': 97715, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 3.5, 'compounds': 'false'}, {'id': 99364, 'type': 'expense', 'name': 'NTIJC FairPrice App PaymenSlNGAPORE', 'amount': 4.03, 'compounds': 'false'}, {'id': 21597, 'type': 'expense', 'name': 'NTUC FairPrice App PaymenSlNGAPORE<br/>Ref No. : 74777154063000603063087', 'amount': 72.58, 'compounds': 'false'}, {'id': 54645, 'type': 'expense', 'name': 'CHICHA SAN CHEN - WATERWASINGAPORE<br/>Ref No. : 74508984061017064944892', 'amount': 23.0, 'compounds': 'false'}, {'id': 49165, 'type': 'expense', 'name': 'NTUC FairPrice App PaymenSlNGAPORE', 'amount': 23.23, 'compounds': 'false'}, {'id': 42139, 'type': 'expense', 'name': 'GIANT-SIMEI MRT SINGAPORE<br/>Ref No. : 74541834059288071971489', 'amount': 2.75, 'compounds': 'false'}, {'id': 51774, 'type': 'expense', 'name': 'AMAR AND CO CAFFE PTE SINGAPORE', 'amount': 6.8, 'compounds': 'false'}, {'id': 28794, 'type': 'expense', 'name': 'BUS/MRT 400545157 SINGAPORE', 'amount': 1.09, 'compounds': 'false'}, {'id': 89890, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 2.9, 'compounds': 'false'}, {'id': 34670, 'type': 'expense', 'name': '7-ELEVEN-225 SIMEI ST 4 SINGAPORE<br/>Ref No. : 74541834062288077878329', 'amount': 1.0, 'compounds': 'false'}, {'id': 41263, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 1.5, 'compounds': 'false'}, {'id': 88256, 'type': 'expense', 'name': 'ANDES CHANG QLUB, SG SINGAPORE', 'amount': 18.9, 'compounds': 'false'}, {'id': 85582, 'type': 'expense', 'name': 'TAKAGI RAMEN-SIMEI SINGAPORE<br/>Ref No. : 74103804059000004330672', 'amount': 11.5, 'compounds': 'false'}, {'id': 55561, 'type': 'expense', 'name': 'UOB ONE CASH REBATE BILL REDEMPTION', 'amount': 200.0, 'compounds': 'false'}, {'id': 23572, 'type': 'expense', 'name': '7-ELEVEN-ORCHARD MRT SINGAPORE', 'amount': 2.4, 'compounds': 'false'}, {'id': 99648, 'type': 'expense', 'name': 'PAYMT THRU E-BANK/HOMEB/CYBERB (EP38)', 'amount': 4696.22, 'compounds': 'false'}, {'id': 52318, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE', 'amount': 10.98, 'compounds': 'false'}, {'id': 88652, 'type': 'expense', 'name': 'insta360 camera', 'amount': 850.42, 'compounds': 'false'}, {'id': 66829, 'type': 'expense', 'name': 'SUBWAY - KALLANGWAVE MALLSINGAPORE<br/>Ref No. : 74508984061017066775245', 'amount': 4.0, 'compounds': 'false'}, {'id': 47165, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 1.0, 'compounds': 'false'}, {'id': 97858, 'type': 'expense', 'name': '7-ELEVEN-SIMEI MRT SINGAPORE', 'amount': 2.9, 'compounds': 'false'}, {'id': 59325, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 3.0, 'compounds': 'false'}, {'id': 46870, 'type': 'expense', 'name': 'LLAO LLAO - CCP SINGAPORE', 'amount': 8.0, 'compounds': 'false'}, {'id': 13315, 'type': 'expense', 'name': 'PRIME SUPERMARKET Singapore', 'amount': 14.9, 'compounds': 'false'}, {'id': 57898, 'type': 'expense', 'name': 'GIGA 68255000', 'amount': 18.33, 'compounds': 'false'}, {'id': 71344, 'type': 'expense', 'name': 'Grab* A-6XDGF7DGWJ3X Singapore', 'amount': 34.8, 'compounds': 'false'}, {'id': 49357, 'type': 'expense', 'name': 'ONE CARD ADDITIONAL REBATE', 'amount': 82.38, 'compounds': 'false'}, {'id': 61120, 'type': 'expense', 'name': 'LLAO LLAO - CCP SINGAPORE<br/>Ref No. : 74541834064288086831333', 'amount': 8.9, 'compounds': 'false'}, {'id': 59658, 'type': 'expense', 'name': 'Grab* A-6XUFG4WWWFXF Singapore', 'amount': 2.9, 'compounds': 'false'}, {'id': 43194, 'type': 'expense', 'name': 'WTROLD-TEA-HUT-CHANGI 6586988741', 'amount': 3.0, 'compounds': 'false'}, {'id': 61555, 'type': 'expense', 'name': 'SHOPEE SINGAPORE MP SINGAPORE', 'amount': 15.36, 'compounds': 'false'}, {'id': 35534, 'type': 'expense', 'name': '7-ELEVEN-CHANGI CITY PT SINGAPORE', 'amount': 2.9, 'compounds': 'false'}]