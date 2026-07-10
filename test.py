def manipulate_list():
    # Define an initial list of at least five integers
    numbers = [12, 45, 7, 23, 89]
    print("Initial list:", numbers)

    # Add two new numbers to the list
    numbers.append(56)
    numbers.append(3)
    print("After adding two numbers:", numbers)

    # Remove one number from the list
    numbers.remove(23)  # removes the value 23
    print("After removing one number:", numbers)

    # Sort the list in ascending order
    numbers.sort()
    print("Final sorted list:", numbers)

    return numbers


if __name__ == "__main__":
    manipulate_list()
