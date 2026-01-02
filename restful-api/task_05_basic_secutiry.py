#!/usr/bin/env python3
"""
Task 05: API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, 
    get_jwt_identity, verify_jwt_in_request, get_jwt
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # In production, use environment variable
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key-here'  # Should be different from SECRET_KEY

# Initialize authentication modules
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1", 
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Basic Authentication verification function
@auth.verify_password
def verify_password(username, password):
    """Verify username and password for basic authentication"""
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None

@auth.error_handler
def auth_error():
    """Error handler for basic authentication"""
    return jsonify({"error": "Unauthorized"}), 401

# JWT Error Handlers
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing JWT token"""
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid JWT token"""
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired JWT token"""
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked JWT token"""
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle need for fresh JWT token"""
    return jsonify({"error": "Fresh token required"}), 401

# Routes
@app.route('/')
def home():
    """Home route"""
    return "Welcome to the Flask API!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Basic authentication protected route"""
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """JWT login endpoint"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON"}), 400
        
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Username and password required"}), 400
        
        # Verify credentials
        if username in users and check_password_hash(users[username]['password'], password):
            # Create JWT token with user identity and role
            additional_claims = {"role": users[username]['role']}
            access_token = create_access_token(
                identity=username,
                additional_claims=additional_claims
            )
            return jsonify({"access_token": access_token}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": "Invalid JSON"}), 400

@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """JWT protected route"""
    return "JWT Auth: Access Granted"

@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Admin-only route with role-based access control"""
    try:
        # Get current user identity
        current_user = get_jwt_identity()
        
        # Get JWT claims to check role
        claims = get_jwt()
        
        # Check if user has admin role
        if claims.get('role') == 'admin':
            return "Admin Access: Granted"
        else:
            return jsonify({"error": "Admin access required"}), 403
    except Exception:
        return jsonify({"error": "Admin access required"}), 403

if __name__ == '__main__':
    app.run(debug=True)
