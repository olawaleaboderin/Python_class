#Coke Machine
# This program simulates a vending machine that sells coke for 50 cents.

def main():
    price = 50
    # cost of one Coke
    amount_due = price

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        # Accept only valid denominations
        if coin in [25, 10, 5]:
            amount_due -= coin
        else:
            # Ignore invalid coins
            continue

    # If user overpays, calculate change
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()
