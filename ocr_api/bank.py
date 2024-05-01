import os
import google.generativeai as genai
from datetime import datetime

class BankStatementProcessor:
    
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-pro')

    def convertGeminiTableToList(self, gemini_response_text, userId):
        lines = gemini_response_text.strip().split('\n')
        # Remove the header and the separator lines
        lines = lines[2:]
        # Initialize list of dict to store transactions
        transactions = []
        for line in lines:
            # Detect end of transactions
            if line == '' or '-next page-' in line:
                break
            # Strip the leading and trailing '|' and split by '|'
            parts = [part.strip() for part in line.split('|')]
            # Extract the fields
            trans_date = parts[1]
            desc = parts[2]
            amount_str = parts[3].replace(',', '').replace('SGD', '').strip() # Remove 'SGD' and ','
            category = parts[4]
            type_str = 'debit'
            # Check if the amount is a credit and handle it
            if 'CR' in amount_str:
                # Remove 'CR', strip any whitespace, and convert to float
                amount = float(amount_str.replace('CR', '').strip())
                # Set 'type' as credit
                type_str = 'credit'
            else:
                # Strip any whitespace, and convert to float
                amount = float(amount_str.strip())
            # Create a dictionary for the transaction
            transaction = {
                'transDate': self.convertStringToDatetime(trans_date),
                'desc': desc,
                'amount': amount,
                'type': type_str,
                'userId': userId,
                'category': category
            }
            # Add the dictionary to the list
            transactions.append(transaction)
        # Check for 'PREVIOUS BALANCE'
        transactions = self.checkForPreviousBalance(transactions)

        return transactions
    
    def checkForPreviousBalance(self, transactions):
        # Variable to keep track of the last valid transaction date
        last_valid_date = None
        # Check if the first transaction has 'PREVIOUS BALANCE' and handle it
        if 'PREVIOUS BALANCE' in transactions[0]['desc']:
            last_valid_date = transactions[0]['transDate']
            # Remove "PREVIOUS BALANCE"
            transactions.pop(0)
            # Iterate through the modified list
            for transaction in transactions:
                if last_valid_date is not None:
                    current_valid_date = transaction['transDate']
                    # Update transDate to previous transDate, last_valid_date
                    transaction['transDate'] = last_valid_date
                last_valid_date = current_valid_date
        return transactions

    def convertStringToDatetime(self, trans_date_str):
        # Assuming current year is appropriate for conversion
        current_year = datetime.now().year
        # Combine the current year with the provided date string
        full_date_str = f"{trans_date_str} {current_year}"
        # Create a datetime object using strptime
        date_format = "%d %b %Y"
        trans_date = datetime.strptime(full_date_str, date_format)
        return trans_date

