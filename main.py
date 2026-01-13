from utils.file_handler import load_sales_data
from utils.data_processor import clean_sales_data
from utils.api_handler import fetch_product_info

def main():
    # Load data
    df = load_sales_data("data/sales_data.txt")

    # Clean data
    cleaned_df = clean_sales_data(df)

    # Enrich data with API info
    cleaned_df['ProductCategory'] = cleaned_df['ProductID'].apply(fetch_product_info)

    # Save cleaned output
    cleaned_df.to_csv("output/cleaned_sales_data.csv", index=False)

    print("Cleaned data saved to output/cleaned_sales_data.csv")

if __name__ == "__main__":
    main()
