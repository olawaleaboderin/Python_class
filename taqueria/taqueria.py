# Program that lets users order from a menu and shows running total.

def main():
    # Define the menu dictionary inside the main() function
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0

    while True:
        try:
            item = input("Item: ").title().strip()
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            print()  # Move to a new line
            break


if __name__ == "__main__":
    main()
