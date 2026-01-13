import requests

def fetch_product_info(product_id):
    """
    Simulated API call to fetch product details.
    """
    mock_api_response = {
        "P101": "Laptop",
        "P102": "Mouse",
        "P103": "Keyboard",
        "P104": "Monitor",

    return mock_api_response.get(product_id, "Unknown Product")
