def clean_sales_data(df):
    """
    Cleans sales transaction data based on given criteria.
    """

    total_records = len(df)

    # Clean UnitPrice (remove commas and spaces)
    df['UnitPrice'] = (
        df['UnitPrice']
        .astype(str)
        .str.replace(',', '')
        .str.replace(' ', '')
        .astype(float)
    )

    # Ensure TransactionID is string
    df['TransactionID'] = df['TransactionID'].astype(str)

    # Define invalid records
    invalid_condition = (
        df['CustomerID'].isna() |
        df['Region'].isna() |
        (df['Quantity'] <= 0) |
        (df['UnitPrice'] <= 0) |
        (~df['TransactionID'].str.startswith('T', na=False))
    )

    invalid_records = df.loc[invalid_condition]
    valid_records = df.loc[~invalid_condition]

    # Clean ProductName
    valid_records['ProductName'] = (
        valid_records['ProductName']
        .str.replace(',', '')
        .str.strip()
    )

    valid_records.reset_index(drop=True, inplace=True)

    # Validation Output
    print(f"Total records parsed: {total_records}")
    print(f"Invalid records removed: {len(invalid_records)}")
    print(f"Valid records after cleaning: {len(valid_records)}")

    return valid_records
