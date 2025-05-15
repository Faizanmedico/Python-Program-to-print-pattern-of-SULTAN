__author__ = 'Your Name'  # Replace with your name

def get_s_pattern(n):
    """Returns the 'S' pattern as a list of strings."""
    pattern = []
    for row in range(n):
        line = ""
        for col in range(n):
            if ((row == 0 or row == n // 2 or row == n - 1) and col > 0 and col < n - 1) or \
               (col == 0 and row < n // 2) or \
               (col == n - 1 and row > n // 2):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def get_u_pattern(n):
    """Returns the 'U' pattern as a list of strings."""
    pattern = []
    for row in range(n):
        line = ""
        for col in range(n):
            if ((col == 0 or col == n - 1) and row < n - 1) or \
               (row == n - 1 and col > 0 and col < n - 1):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def get_l_pattern(n):
    """Returns the 'L' pattern as a list of strings."""
    pattern = []
    for row in range(n):
        line = ""
        for col in range(n):
            if col == 0 or row == n - 1:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def get_t_pattern(n):
    """Returns the 'T' pattern as a list of strings."""
    pattern = []
    for row in range(n):
        line = ""
        for col in range(n):
            if row == 0 or col == n // 2:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def get_a_pattern(n):
    """Returns the 'A' pattern as a list of strings."""
    pattern = []
    for row in range(n):
        line = ""
        for col in range(n):
            if ((col == 0 or col == n - 1) and row != 0) or \
               (row == 0 and col > 0 and col < n - 1) or \
               (row == n // 2 and col > 0 and col < n - 1):
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def get_n_pattern(n):
    """Returns the 'N' pattern as a list of strings."""
    pattern = []
    for row in range(n):
        line = ""
        for col in range(n):
            if col == 0 or col == n - 1 or row == col:
                line += "*"
            else:
                line += " "
        pattern.append(line)
    return pattern

def print_name_horizontal(name, size):
    """Prints the given name pattern in horizontal lines."""
    if size < 8:
        print("Enter a size greater than 8 for better visibility.")
        return

    name_patterns = {
        'S': get_s_pattern,
        'U': get_u_pattern,
        'L': get_l_pattern,
        'T': get_t_pattern,
        'A': get_a_pattern,
        'N': get_n_pattern,
    }

    letter_patterns = []
    for char in name.upper():
        if char in name_patterns:
            letter_patterns.append(name_patterns[char](size + 2)) # Get pattern for each letter
        else:
            print(f"Character '{char}' not supported in the pattern.")
            return

    # Determine the number of rows (based on the size of the letters)
    num_rows = len(letter_patterns[0])

    # Print the letters horizontally, line by line
    for i in range(num_rows):
        line = ""
        for pattern in letter_patterns:
            line += pattern[i] + "  "  # Add spacing between letters
        print(line)

if __name__ == "__main__":
    size = int(input("Enter size: \t"))
    print_name_horizontal("Sultan", size)