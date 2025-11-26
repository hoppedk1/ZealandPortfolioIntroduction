import random
import string

def generate_password(length=12): 
    # Symbols to exclude (commonly problematic in databases)
    exclude_symbols = {'"', "'", '\\', ';', '`', '.', ',', '+', '@'} # kan altid tilføje flere her
    # Build the allowed character set
    chars = (
        string.ascii_letters +
        string.digits +
        ''.join(c for c in string.punctuation if c not in exclude_symbols)
    )
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage
print(generate_password(16))