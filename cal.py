"""
A simple command line calculator that performs addition and multiplication
"""


def get_numbers():
    numbers = []
    print("Enter numbers (type 'done' when finished): ")

    while True:
        user_input = input("Enter a number: ").strip()

        if user_input.lower() == 'done':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number.")

    return numbers


def add_numbers(numbers):
    """Return the sum of numbers"""
    return sum(numbers)


def multiply_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def main():
    print("=" * 50)
    print("Welcome to the Collaborative Cal")
    print("=" * 50)
    numbers = get_numbers()
    if len(numbers) == 0:
        print("No numbers entered exists")
        return
    print(f"\n You entered: {numbers}")
    print("\n What operation would you like to perform?")
    print("1. Add")
    print("2.Mutiply")

    # choice = input("enter your choice (1 or 2): ")

    choice = input("enter ").strip()
    if choice == '1':
        result = add_numbers(numbers)
        print(f"\n Result: {' + '.join(map(str, numbers))} = {result}")
    elif choice == '2':
        result = multiply_numbers(numbers)
        print(f"\n Result: {' + '.join(map(str, numbers))} = {result}")
    else:
        print("invalid choice")


if __name__ == "__main__":
    main()
