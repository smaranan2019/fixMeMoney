gemini_prompt =  """Given:
- The columns are 'Trans Date' (date), 'Description of Transaction' (string), 'Transaction Amount' (decimal).
- Exclude 'Post' column and its values.
- Ignore 'Ref No.' only.
- Add column 'Category' (string) and categorize each row into [food, travel, apparel, transport, bills, medical expenses, subscriptions, tax, others].
Convert the following text into table data:"""

ocr_url = 'https://api.ocr.space/parse/image'

ALLOWED_EXTENSIONS_PDF = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_PDF