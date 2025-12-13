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
    choice = input("enter ")


if __name__ == "__main__":
    main()
