
#!/usr/bin/env python3
"""
Flask application to display product data from JSON or CSV files.
"""

from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)


def read_json_products(file_path='products.json'):
    """Read and parse products from JSON file."""
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return json.load(file)
        return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading JSON file: {e}")
        return []


def read_csv_products(file_path='products.csv'):
    """Read and parse products from CSV file."""
    products = []
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert id and price to appropriate types
                    product = {
                        'id': int(row['id']) if row.get('id') else 0,
                        'name': row.get('name', ''),
                        'category': row.get('category', ''),
                        'price': float(row['price']) if row.get('price') else 0.0
                    }
                    products.append(product)
    except (csv.Error, IOError, ValueError) as e:
        print(f"Error reading CSV file: {e}")
    return products


@app.route('/products')
def display_products():
    """
    Display products from JSON or CSV file.
    
    Query parameters:
    - source: 'json' or 'csv' (required)
    - id: product id to filter (optional)
    """
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv']:
        return render_template('product_display.html', 
                             error=f"Wrong source: '{source}'. Use 'json' or 'csv'.")
    
    # Read products based on source
    if source == 'json':
        products = read_json_products()
    else:  # source == 'csv'
        products = read_csv_products()
    
    # Filter by id if provided
    if product_id:
        try:
            product_id_int = int(product_id)
            filtered_products = [p for p in products if p.get('id') == product_id_int]
            
            if not filtered_products:
                # Return exact error message as specified in requirements
                return render_template('product_display.html',
                                     error="Product not found")
            
            products = filtered_products
        except ValueError:
            return render_template('product_display.html',
                                 error=f"Invalid product id: '{product_id}'.")
    
    # Check if we have any products
    if not products:
        return render_template('product_display.html',
                             error="No products found in the data file.")
    
    return render_template('product_display.html', 
                         products=products, 
                         source=source,
                         product_id=product_id)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
