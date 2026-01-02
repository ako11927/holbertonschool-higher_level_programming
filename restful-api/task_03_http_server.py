#!/usr/bin/env python3
"""
Task 03: Develop a simple API using Python with the `http.server` module

"""

import http.server
import json
from http import HTTPStatus

class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for a simple API server.
    """
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints.
        """
        # Route based on the path
        if self.path == '/':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            
            # Create JSON response
            response_data = {"name": "Ahmed", "age": 36, "city": "Riyadh"}
            response_json = json.dumps(response_data)
            self.wfile.write(response_json.encode('utf-8'))
        
        elif self.path == '/status':
            self.send_response(HTTPStatus.OK)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            # Handle undefined endpoints
            self.send_response(HTTPStatus.NOT_FOUND)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
    
    def log_message(self, format, *args):
        """
        Override to prevent default logging to stderr.
        """
        pass

def main():
    """
    Main function to start the server.
    """
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleAPIHandler)
    
    print("Starting server on port 8000...")
    print("Available endpoints:")
    print("  http://localhost:8000/")
    print("  http://localhost:8000/data")
    print("  http://localhost:8000/status")
    print("Press Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()
