#!/usr/bin/env python3
"""
Flask application to display product data from JSON, CSV, or SQLite database.
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3
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


def read_sql_products(db_path='products.db'):
    """Read and parse products from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # This allows column access by name
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        for row in rows:
            product = {
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            }
            products.append(product)
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Error reading SQLite database: {e}")
    return products


@app.route('/products')
def display_products():
    """
    Display products from JSON, CSV, or SQLite database.
    
    Query parameters:
    - source: 'json', 'csv', or 'sql' (required)
    - id: product id to filter (optional)
    """
    # Get query parameters
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error=f"Wrong source: '{source}'. Use 'json', 'csv', or 'sql'.")
    
    # Read products based on source
    if source == 'json':
        products = read_json_products()
    elif source == 'csv':
        products = read_csv_products()
    else:  # source == 'sql'
        products = read_sql_products()
    
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
                             error="No products found in the data source.")
    
    return render_template('product_display.html', 
                         products=products, 
                         source=source,
                         product_id=product_id)


@app.route('/test')
def test_page():
    """Test page with example URLs."""
    return """
    <!DOCTYPE html>
    <html>
    <head><title>Test URLs</title></head>
    <body>
        <h1>Test Product Display with Multiple Sources</h1>
        
        <h2>JSON Examples:</h2>
        <ul>
            <li><a href="/products?source=json">All JSON products</a></li>
            <li><a href="/products?source=json&id=1">JSON product id=1</a></li>
        </ul>
        
        <h2>CSV Examples:</h2>
        <ul>
            <li><a href="/products?source=csv">All CSV products</a></li>
            <li><a href="/products?source=csv&id=2">CSV product id=2</a></li>
        </ul>
        
        <h2>SQL Examples:</h2>
        <ul>
            <li><a href="/products?source=sql">All SQL products</a></li>
            <li><a href="/products?source=sql&id=1">SQL product id=1</a></li>
            <li><a href="/products?source=sql&id=2">SQL product id=2</a></li>
        </ul>
        
        <h2>Error Examples:</h2>
        <ul>
            <li><a href="/products?source=xml">Invalid source (xml)</a></li>
            <li><a href="/products?source=sql&id=999">Product not found (id=999)</a></li>
            <li><a href="/products">Missing source parameter</a></li>
        </ul>
        
        <h2>Database Info:</h2>
        <p>The SQLite database contains the same products as JSON and CSV files.</p>
    </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True, port=5000)
