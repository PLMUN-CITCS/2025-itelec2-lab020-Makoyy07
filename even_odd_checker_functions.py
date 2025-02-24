def get_integer_input() -> int:
    """Prompts the user to enter a valid integer and returns it."""
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")

def check_even_odd(number: int) -> str:
    """Determines whether the given number is even or odd."""
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """Main function to execute the even-odd checker."""
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()