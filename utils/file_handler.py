#!/usr/bin/env python
# coding: utf-8

# In[1]:


def read_sales_data(filename):
    encodings = ['utf-8', 'latin-1', 'cp1252']

    for encoding in encodings:
        try:
            with open(filename, 'r', encoding=encoding) as file:
                lines = file.readlines()

            # Skip header and remove empty lines
            return [line.strip() for line in lines[1:] if line.strip()]

        except UnicodeDecodeError:
            continue
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return []

    print("Error: Unable to read file due to encoding issues.")
    return []


# In[2]:


def parse_transactions(raw_lines):
    transactions = []

    for line in raw_lines:
        parts = line.split('|')

        if len(parts) != 8:
            continue  # skip invalid rows

        try:
            transaction = {
                'TransactionID': parts[0],
                'Date': parts[1],
                'ProductID': parts[2],
                'ProductName': parts[3].replace(',', ''),
                'Quantity': int(parts[4].replace(',', '')),
                'UnitPrice': float(parts[5].replace(',', '')),
                'CustomerID': parts[6],
                'Region': parts[7]
            }
            transactions.append(transaction)

        except ValueError:
            continue  # skip rows with invalid data

    return transactions


# In[3]:


def validate_and_filter(transactions, region=None, min_amount=None, max_amount=None):
    valid = []
    invalid = 0

    regions = set(t['Region'] for t in transactions)
    amounts = [t['Quantity'] * t['UnitPrice'] for t in transactions]

    print("Available regions:", regions)
    print("Transaction amount range:", min(amounts), "-", max(amounts))

    filtered_by_region = 0
    filtered_by_amount = 0

    for t in transactions:
        if (
            t['Quantity'] <= 0 or
            t['UnitPrice'] <= 0 or
            not t['TransactionID'].startswith('T') or
            not t['ProductID'].startswith('P') or
            not t['CustomerID'].startswith('C')
        ):
            invalid += 1
            continue

        amount = t['Quantity'] * t['UnitPrice']

        if region and t['Region'] != region:
            filtered_by_region += 1
            continue

        if min_amount and amount < min_amount:
            filtered_by_amount += 1
            continue

        if max_amount and amount > max_amount:
            filtered_by_amount += 1
            continue

        valid.append(t)

    summary = {
        'total_input': len(transactions),
        'invalid': invalid,
        'filtered_by_region': filtered_by_region,
        'filtered_by_amount': filtered_by_amount,
        'final_count': len(valid)
    }

    return valid, invalid, summary


# In[ ]:




