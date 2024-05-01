import firebase_admin
from firebase_admin import credentials, firestore
import uuid
from google.cloud.firestore_v1.base_query import FieldFilter

class Database:
    def __init__(self, cred):
        firebase_admin.initialize_app(cred)
        self.cred = cred
        self.db = firestore.client()

    def saveToDb(self, transactions_list):
        # Add a new doc (transaction) in collection 'transactions'
        # Each doc's id is randomly generated uuid
        for transaction in transactions_list:
            self.db.collection("transactions").document(str(uuid.uuid4())).set(transaction)

    def queryTransactionsForUserToConfirm(self, userId):
        # Create a reference to the transactions collection
        transactions_ref = self.db.collection("transactions")
        # Create a query against the 'transactions' collection for user which have not been confirmed
        user_transactions_ref = transactions_ref.where(filter=FieldFilter("userId", "==", userId)).where(filter=FieldFilter("userConfirm", "==", False)).stream()
        transactions = []
        for transaction in user_transactions_ref:
            if transaction.exists:
                transaction_data = transaction.to_dict()
                transaction_data['id'] = transaction.id  # Include the document ID in the data
                transactions.append(transaction_data)
        return transactions
