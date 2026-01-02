#!/usr/bin/env python3
"""
Task 04: Develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with empty users dictionary
users = {}

@app.route('/')
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    """Return all usernames as JSON array"""
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """API status endpoint"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Get user by username"""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user - handles POST requests"""
    try:
        # Get JSON data from request
        data = request.get_json(force=True, silent=True)
        
        # Check if JSON is valid
        if data is None:
            return jsonify({"error": "Invalid JSON"}), 400
        
        # Check if username is provided
        if "username" not in data:
            return jsonify({"error": "Username is required"}), 400
        
        username = data["username"]
        
        # Check if username already exists
        if username in users:
            return jsonify({"error": "Username already exists"}), 409
        
        # Create user object with provided data
        user_data = {
            "username": username,
            "name": data.get("name", ""),
            "age": data.get("age"),
            "city": data.get("city", "")
        }
        
        # Add user to dictionary
        users[username] = user_data
        
        # Return success response
        return jsonify({
            "message": "User added",
            "user": user_data
        }), 201
        
    except Exception:
        # Catch any parsing errors
        return jsonify({"error": "Invalid JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
