__author__ = 'Your Name'  # Replace with your name

def print_s(n):
    """Prints the letter 'S' pattern."""
    for row in range(n):
        for col in range(n):
            if ((row == 0 or row == n // 2 or row == n - 1) and col > 0 and col < n - 1) or \
               (col == 0 and row < n // 2) or \
               (col == n - 1 and row > n // 2):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_u(n):
    """Prints the letter 'U' pattern."""
    for row in range(n):
        for col in range(n):
            if ((col == 0 or col == n - 1) and row < n - 1) or \
               (row == n - 1 and col > 0 and col < n - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_l(n):
    """Prints the letter 'L' pattern."""
    for row in range(n):
        for col in range(n):
            if col == 0 or row == n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_t(n):
    """Prints the letter 'T' pattern."""
    for row in range(n):
        for col in range(n):
            if row == 0 or col == n // 2:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_a(n):
    """Prints the letter 'A' pattern."""
    for row in range(n):
        for col in range(n):
            if ((col == 0 or col == n - 1) and row != 0) or \
               (row == 0 and col > 0 and col < n - 1) or \
               (row == n // 2 and col > 0 and col < n - 1):
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_n(n):
    """Prints the letter 'N' pattern."""
    for row in range(n):
        for col in range(n):
            if col == 0 or col == n - 1 or row == col:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def print_name(name, size):
    """Prints the given name pattern."""
    if size < 8:
        print("Enter a size greater than 8 for better visibility.")
        return

    name_patterns = {
        'S': print_s,
        'U': print_u,
        'L': print_l,
        'T': print_t,
        'A': print_a,
        'N': print_n,
    }

    for char in name.upper():
        if char in name_patterns:
            name_patterns[char](size + 2)  # Adding a little extra size for spacing
        else:
            print(f"Character '{char}' not supported in the pattern.")
        print()  # Add a newline after each letter for spacing

if __name__ == "__main__":
    size = int(input("Enter size: \t"))
    print_name("Sultan", size)