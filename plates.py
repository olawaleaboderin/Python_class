# Vanity Plates
# This program validates a vanity plate based on Massachusetts rules.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Check for invalid characters (only letters and digits allowed)
    if not s.isalnum():
        return False

    # Numbers, if present, must be at the end
    if not numbers_at_end(s):
        return False

    return True


def numbers_at_end(s):
    """Check that if numbers are used, they appear only at the end and don’t start with zero"""
    for i, char in enumerate(s):
        if char.isdigit():
            # Once we see a digit, the rest must all be digits
            if char == "0" and i == len(s) - len(s[i:]):  # first number cannot be '0'
                return False
            if not s[i:].isdigit():
                return False
            break
    return True


if __name__ == "__main__":
    main()
