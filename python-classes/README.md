# Python - Classes and Objects

This project introduces the concept of Object-Oriented Programming (OOP) in Python using classes, objects, attributes, methods, getters, setters, and encapsulation.  
You will create the `Square` class in multiple steps, adding features gradually such as private attributes, data validation, methods, and print formatting.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using **python3 (version 3.8.5)**
- Files must end with a new line
- First line of all Python files must be:
#!/usr/bin/python3

pgsql
Copy code
- Code must follow **pycodestyle** (version 2.7.\*)
- All files must be executable
- The length of your files will be tested using `wc`
- All modules must have documentation
- All classes must have documentation
- All methods and functions must have documentation
- No imports allowed unless specified (for this project: **no imports**)

## Project Structure

|-- python-classes
|-- 0-square.py
|-- 1-square.py
|-- 2-square.py
|-- 3-square.py
|-- 4-square.py
|-- 5-square.py
|-- 6-square.py
|-- README.md

markdown
Copy code

## Tasks Summary

### **0. My first square**
Create an empty class `Square`.

### **1. Square with size**
Add a private instance attribute `__size`.

### **2. Size validation**
Add validation ensuring:
- size must be an integer
- size must be >= 0

### **3. Area of a square**
Add method:
def area(self):

markdown
Copy code
Returns the area of the square.

### **4. Access and update private attribute**
Add:
- Getter `size`
- Setter `size` with validation

### **5. Printing a square**
Add method:
def my_print(self):

perl
Copy code
Prints the square using `#`.

### **6. Coordinates of a square**
Add a new attribute `position` and update printing logic accordingly.
