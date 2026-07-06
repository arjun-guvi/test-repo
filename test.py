def filter_strings(input_list):
    """Return a new list containing only the string elements from input_list."""
    return [item for item in input_list if isinstance(item, str)]


# Simple test case
if __name__ == "__main__":
    sample = [1, "apple", 3.14, "banana", True, "cherry", None, "42"]
    result = filter_strings(sample)
    print(result)  # Expected: ['apple', 'banana', 'cherry', '42']

    assert result == ["apple", "banana", "cherry", "42"], "Test failed!"
    print("Test passed!")
