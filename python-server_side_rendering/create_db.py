#!/usr/bin/env python3
"""
Script to create and populate the SQLite database.
"""

import sqlite3

def create_database():
    """Create and populate the products database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Clear any existing data
    cursor.execute('DELETE FROM Products')
    
    # Insert sample data
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99),
        (3, 'Wireless Mouse', 'Electronics', 29.99),
        (4, 'Desk Lamp', 'Home Goods', 45.50),
        (5, 'Notebook', 'Office Supplies', 8.99),
        (6, 'Bluetooth Speaker', 'Electronics', 89.99),
        (7, 'Throw Pillow', 'Home Goods', 24.99),
        (8, 'Stapler', 'Office Supplies', 12.50)
    ''')
    
    conn.commit()
    conn.close()
    print("Database created and populated successfully!")

if __name__ == '__main__':
    create_database()
