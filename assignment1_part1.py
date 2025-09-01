"""
IS211 Assignment 1 — Part 1
Functions and Exceptions
"""

# Custom exception (exactly 2 lines)
class ListDivideException(Exception): 
    pass


def list_divide(numbers, divide=2):
    """Return the number of elements in `numbers` divisible by `divide`."""
    if divide == 0:
        raise ValueError("divide must not be zero")
    return sum(1 for number in numbers if number % divide == 0)


def test_list_divide():
    """
    Run the 5 required tests.
    Print each result, and raise ListDivideException if any test fails.
    """
    failures = []

    # Test 1
    result = list_divide([1, 2, 3, 4, 5])
    print("Test 1 result:", result)
    if result != 2:
        failures.append("Test 1 failed")

    # Test 2
    result = list_divide([2, 4, 6, 8, 10])
    print("Test 2 result:", result)
    if result != 5:
        failures.append("Test 2 failed")

    # Test 3
    result = list_divide([30, 54, 63, 98, 100], divide=10)
    print("Test 3 result:", result)
    if result != 2:
        failures.append("Test 3 failed")

    # Test 4
    result = list_divide([])
    print("Test 4 result:", result)
    if result != 0:
        failures.append("Test 4 failed")

    # Test 5
    result = list_divide([1, 2, 3, 4, 5], 1)
    print("Test 5 result:", result)
    if result != 5:
        failures.append("Test 5 failed")

    if failures:
        # Raise exactly as the assignment requires
        raise ListDivideException("; ".join(failures))
    else:
        print("All tests passed.")


if __name__ == "__main__":
    test_list_divide()
