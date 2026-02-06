#!/usr/bin/env python3
"""
Flask application with dynamic templates using loops and conditions.
"""

from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    """Render the items page with dynamic content."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
