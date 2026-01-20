import sys
import os

sys.path.append(os.getcwd())


from utils.file_handler import read_sales_data
from utils.data_processor import (
    parse_sales_data,
    daily_sales_trend,
    find_peak_sales_day,
    low_performing_products,
    enrich_sales_data,
    save_enriched_data,
    generate_sales_report
)
from utils.api_handler import fetch_all_products, create_product_mapping


def main():
    print("=" * 30)
    print("SALES ANALYTICS SYSTEM")
    print("=" * 30)

    # Step 1: Read sales data
    raw_data = read_sales_data('data/sales_data.txt')
    print("✔ Sales data read")

    # Step 2: Parse & clean
    transactions = parse_sales_data(raw_data)
    print(f"✔ Parsed {len(transactions)} records")

    # Step 3: Analysis
    daily_trend = daily_sales_trend(transactions)
    peak_day = find_peak_sales_day(transactions)
    low_products = low_performing_products(transactions)

    print("✔ Analysis completed")

    # Step 4: API Integration
    api_products = fetch_all_products()
    product_mapping = create_product_mapping(api_products)

    # Step 5: Enrich sales data
    enriched_data = enrich_sales_data(transactions, product_mapping)
    save_enriched_data(enriched_data)
    print("✔ Enriched data saved")

    # Step 6: Generate report
    generate_sales_report(transactions, enriched_data)
    print("✔ Report generated")

    print("\n🎉 PROCESS COMPLETED SUCCESSFULLY")


if __name__ == "__main__":
    main()
