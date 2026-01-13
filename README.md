# Sales Analytics System

## Overview
This project implements a Python-based sales analytics system for an e-commerce company.  
It cleans messy transaction data, validates records, enriches data using API calls, and prepares clean data for analysis.

## Features
- Reads pipe-separated TXT sales files
- Removes invalid records
- Cleans product names and numeric fields
- Fetches product information from an API
- Generates cleaned output for analysis

## Project Structure
- main.py: Entry point of the application
- utils/: Helper modules
- data/: Input dataset
- output/: Generated reports

## How to Run
```bash
pip install -r requirements.txt
python main.py
