import pandas as pd

def load_sales_data(file_path):
    """
    Reads pipe-separated sales data from a TXT file.
    """
    df = pd.read_csv(
        file_path,
        delimiter='|',
        skip_blank_lines=True
    )
    return df
