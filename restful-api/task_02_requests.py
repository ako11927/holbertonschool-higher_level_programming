#!/usr/bin/env python3
"""
Task 02: Consuming and processing data from an API using Python
"""

import requests
import csv
from typing import List, Dict, Any

def fetch_and_print_posts() -> None:
    """
    Fetches posts from JSONPlaceholder and prints the status code and post titles.
    
    Returns:
        None
    """
    # Send GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Iterate through posts and print titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts() -> None:
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    
    Returns:
        None
    """
    # Send GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Structure data into list of dictionaries with specific keys
        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)
        
        # Write data to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define the fieldnames/column headers
            fieldnames = ['id', 'title', 'body']
            
            # Create DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            writer.writeheader()
            
            # Write all the posts
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")

# Alternative version using list comprehension (more concise):
def fetch_and_save_posts_comprehension() -> None:
    """
    Alternative implementation using list comprehension for more concise code.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        
        # Using list comprehension to structure data
        structured_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")#!/usr/bin/env python3
"""
Task 02: Consuming and processing data from an API using Python
"""

import requests
import csv
from typing import List, Dict, Any

def fetch_and_print_posts() -> None:
    """
    Fetches posts from JSONPlaceholder and prints the status code and post titles.
    
    Returns:
        None
    """
    # Send GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # Print the status code
    print(f"Status Code: {response.status_code}")
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Iterate through posts and print titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts() -> None:
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    
    Returns:
        None
    """
    # Send GET request to JSONPlaceholder API
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    # If the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()
        
        # Structure data into list of dictionaries with specific keys
        structured_posts = []
        for post in posts:
            structured_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            structured_posts.append(structured_post)
        
        # Write data to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define the fieldnames/column headers
            fieldnames = ['id', 'title', 'body']
            
            # Create DictWriter object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            writer.writeheader()
            
            # Write all the posts
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")

# Alternative version using list comprehension (more concise):
def fetch_and_save_posts_comprehension() -> None:
    """
    Alternative implementation using list comprehension for more concise code.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if response.status_code == 200:
        posts = response.json()
        
        # Using list comprehension to structure data
        structured_posts = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(structured_posts)
        
        print("Data has been saved to posts.csv")
