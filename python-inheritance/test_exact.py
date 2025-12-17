#!/usr/bin/python3
import sys

try:
    BaseGeometry = __import__('7-base_geometry').BaseGeometry
    bg = BaseGeometry()
    
    print("1. Testing method exists...")
    if hasattr(bg, 'integer_validator'):
        print("   ✓ integer_validator exists")
    else:
        print("   ✗ integer_validator NOT FOUND")
        sys.exit(1)
    
    print("\n2. Testing exact error messages...")
    
    # Test 1: String input
    try:
        bg.integer_validator("age", "hello")
        print("   ✗ Should have raised TypeError for string")
    except TypeError as e:
        if str(e) == "age must be an integer":
            print("   ✓ Correct TypeError message")
        else:
            print(f"   ✗ Wrong message: '{e}' (expected: 'age must be an integer')")
    
    # Test 2: Zero
    try:
        bg.integer_validator("width", 0)
        print("   ✗ Should have raised ValueError for 0")
    except ValueError as e:
        if str(e) == "width must be greater than 0":
            print("   ✓ Correct ValueError message")
        else:
            print(f"   ✗ Wrong message: '{e}' (expected: 'width must be greater than 0')")
    
    # Test 3: Negative
    try:
        bg.integer_validator("height", -5)
        print("   ✗ Should have raised ValueError for -5")
    except ValueError as e:
        if str(e) == "height must be greater than 0":
            print("   ✓ Correct ValueError message for negative")
        else:
            print(f"   ✗ Wrong message: '{e}'")
    
    # Test 4: Boolean True (special case)
    try:
        bg.integer_validator("test", True)
        print("   ✗ Should have raised TypeError for True")
    except TypeError as e:
        print(f"   ✓ Raises TypeError for True: {e}")
    
    # Test 5: Valid input
    try:
        bg.integer_validator("size", 10)
        print("   ✓ Accepts valid integer 10")
    except:
        print("   ✗ Should accept valid integer")
    
    print("\n3. Testing area method...")
    try:
        bg.area()
        print("   ✗ area() should raise Exception")
    except Exception as e:
        if str(e) == "area() is not implemented":
            print("   ✓ area() raises correct exception")
        else:
            print(f"   ✗ area() wrong message: '{e}'")
            
except Exception as e:
    print(f"\nERROR: {type(e).__name__}: {e}")
