'''Q3. Data Extraction – Invoice Parser

You are given a string containing multiple invoices in this format:
Write a Python program using regex that extracts:

Invoice number

Date

Amount

Store the extracted data into a dictionary list and print it.'''

import re


def extract_invoice_data(invoice_text):
    invoice_pattern = r"Invoice No: (\d+) \| Date: (\d{4}-\d{2}-\d{2}) \| Amount: (\d+) Rs"

    invoices = []

    matches = re.findall(invoice_pattern, invoice_text)

    for match in matches:
        invoice_data = {
            'Invoice No': match[0],
            'Date': match[1],
            'Amount': match[2]
        }
        invoices.append(invoice_data)

    return invoices


invoice_text = """
Invoice No: 101 | Date: 2025-09-10 | Amount: 2500 Rs
Invoice No: 102 | Date: 2025-09-12 | Amount: 3000 Rs
Invoice No: 103 | Date: 2025-09-13 | Amount: 4500 Rs
"""

extracted_data = extract_invoice_data(invoice_text)
print(extracted_data)
