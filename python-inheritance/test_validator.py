#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

# Test all the cases mentioned in the screenshot
tests = [
    # (name, value, expected_exception_class, description)
    ("name", "John", "TypeError", "string instead of int"),
    ("age", 0, "ValueError", "zero value"),
    ("distance", -4, "ValueError", "negative value"),
    ("age", 1, None, "valid integer"),
    ("age", "4", "TypeError", "string number"),
    ("age", (4, 1), "TypeError", "tuple"),
    ("age", [3], "TypeError", "list"),
    ("age", True, "TypeError", "boolean True"),
    ("age", [3, 4], "TypeError", "list of ints"),
    ("age", None, "TypeError", "None"),
]

print("Running tests...")
all_passed = True

for name, value, expected_exc, desc in tests:
    try:
        bg.integer_validator(name, value)
        if expected_exc is None:
            print(f"✓ {desc}: PASSED")
        else:
            print(f"✗ {desc}: FAILED - Expected {expected_exc} but got no exception")
            all_passed = False
    except TypeError as e:
        if expected_exc == "TypeError":
            print(f"✓ {desc}: PASSED - Got TypeError: {e}")
        else:
            print(f"✗ {desc}: FAILED - Expected {expected_exc} but got TypeError: {e}")
            all_passed = False
    except ValueError as e:
        if expected_exc == "ValueError":
            print(f"✓ {desc}: PASSED - Got ValueError: {e}")
        else:
            print(f"✗ {desc}: FAILED - Expected {expected_exc} but got ValueError: {e}")
            all_passed = False
    except Exception as e:
        print(f"✗ {desc}: FAILED - Got unexpected {type(e).__name__}: {e}")
        all_passed = False

if all_passed:
    print("\n✅ All tests passed!")
else:
    print("\n❌ Some tests failed!")
