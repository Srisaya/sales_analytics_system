#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_total_revenue(transactions):
    return sum(t['Quantity'] * t['UnitPrice'] for t in transactions)


# In[2]:


def get_region_sales(transactions):
    region_sales = {}

    for t in transactions:
        region = t['Region']
        amount = t['Quantity'] * t['UnitPrice']
        region_sales[region] = region_sales.get(region, 0) + amount

    return region_sales


# In[3]:


def get_top_selling_products(transactions, top_n=5):
    product_sales = {}

    for t in transactions:
        product = t['ProductName']
        product_sales[product] = product_sales.get(product, 0) + t['Quantity']

    return sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:top_n]


# In[4]:


def analyze_customer_purchases(transactions):
    customers = {}

    for t in transactions:
        customer = t['CustomerID']
        amount = t['Quantity'] * t['UnitPrice']
        customers[customer] = customers.get(customer, 0) + amount

    return customers


# In[5]:


from collections import defaultdict

def daily_sales_trend(transactions):
    result = defaultdict(lambda: {
        'revenue': 0,
        'transaction_count': 0,
        'unique_customers': set()
    })

    for t in transactions:
        date = t['Date']
        result[date]['revenue'] += t['Quantity'] * t['UnitPrice']
        result[date]['transaction_count'] += 1
        result[date]['unique_customers'].add(t['CustomerID'])

    final = {}
    for date in sorted(result):
        final[date] = {
            'revenue': result[date]['revenue'],
            'transaction_count': result[date]['transaction_count'],
            'unique_customers': len(result[date]['unique_customers'])
        }

    return final


# In[6]:


def find_peak_sales_day(transactions):
    daily = daily_sales_trend(transactions)
    peak = max(daily.items(), key=lambda x: x[1]['revenue'])
    return peak[0], peak[1]['revenue'], peak[1]['transaction_count']


# In[7]:


from collections import defaultdict

def low_performing_products(transactions, threshold=10):
    products = defaultdict(lambda: {'qty': 0, 'revenue': 0})

    for t in transactions:
        products[t['ProductName']]['qty'] += t['Quantity']
        products[t['ProductName']]['revenue'] += t['Quantity'] * t['UnitPrice']

    result = [
        (name, v['qty'], v['revenue'])
        for name, v in products.items()
        if v['qty'] < threshold
    ]

    return sorted(result, key=lambda x: x[1])


# In[8]:


def generate_sales_report(transactions, enriched_transactions, output_file='output/sales_report.txt'):
    """
    Generates a comprehensive sales analysis report
    """

    from datetime import datetime
    from collections import defaultdict

    total_revenue = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
    total_transactions = len(transactions)
    avg_order_value = total_revenue / total_transactions if total_transactions else 0

    dates = [t['Date'] for t in transactions]
    date_range = f"{min(dates)} to {max(dates)}" if dates else "N/A"

    region_sales = defaultdict(float)
    for t in transactions:
        region_sales[t['Region']] += t['Quantity'] * t['UnitPrice']

    api_matches = sum(1 for t in enriched_transactions if t.get('API_Match'))
    api_success_rate = (api_matches / len(enriched_transactions)) * 100 if enriched_transactions else 0

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("SALES ANALYSIS REPORT\n")
        f.write("=" * 30 + "\n")
        f.write(f"Generated On: {datetime.now()}\n")
        f.write(f"Total Records: {total_transactions}\n\n")

        f.write("OVERALL SUMMARY\n")
        f.write(f"Total Revenue: ₹{total_revenue:,.2f}\n")
        f.write(f"Average Order Value: ₹{avg_order_value:,.2f}\n")
        f.write(f"Date Range: {date_range}\n\n")

        f.write("REGIONAL PERFORMANCE\n")
        for region, revenue in region_sales.items():
            f.write(f"{region}: ₹{revenue:,.2f}\n")

        f.write("\nAPI ENRICHMENT SUMMARY\n")
        f.write(f"API Success Rate: {api_success_rate:.2f}%\n")

    print("✔ Sales report generated successfully")


# In[ ]:




