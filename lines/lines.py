import sys
import os

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    count = count_lines(filename)
    print(count)

def count_lines(filename):
    count = 0
    inside_docstring = False
    with open(filename) as file:
        for line in file:
            line = line.strip()

            # Handle docstrings
            if line.startswith('"""') or line.startswith("'''"):
                inside_docstring = not inside_docstring
                continue
            if inside_docstring:
                continue

            if line == "" or line.startswith("#"):
                continue

            count += 1
    return count

if __name__ == "__main__":
    main()
