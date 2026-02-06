#!/usr/bin/env python3
"""
Flask application with dynamic templates using loops and conditions.
"""

from flask import Flask, render_template
import json
import os

app = Flask(__name__)


def read_items_from_json():
    """
    Read items from items.json file.
    Returns a list of items, or empty list if file doesn't exist or is invalid.
    """
    try:
        if os.path.exists('items.json'):
            with open('items.json', 'r') as file:
                data = json.load(file)
                return data.get('items', [])
        return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading items.json: {e}")
        return []


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/items')
def items():
    """Render the items page with dynamic content."""
    items_list = read_items_from_json()
    return render_template('items.html', items=items_list)


@app.route('/items/test/<test_type>')
def test_items(test_type):
    """
    Test endpoint to demonstrate different scenarios.
    test_type can be: 'normal', 'empty', 'single'
    """
    test_items = {
        'normal': ["Python Book", "Flask Mug", "Jinja Sticker", 
                   "Web Development", "Database Design"],
        'empty': [],
        'single': ["Just one item"],
        'many': [f"Item {i}" for i in range(1, 21)]  # 20 items
    }
    
    items_list = test_items.get(test_type, ["Test Item 1", "Test Item 2"])
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
