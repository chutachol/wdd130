# Constants for character types
LOWER = list("abcdefghijklmnopqrstuvwxyz")
UPPER = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DIGITS = list("0123456789")
SPECIAL = list("!@#$%^&*()-_=+[]{}|;:\"',.<>?/`~")

# Function to check if a word exists in a file
def word_in_file(word, filename, case_sensitive=False):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if word == line_word:
                        return True
                else:
                    if word.lower() == line_word.lower():
                        return True
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return False

# Function to check if a word contains any character from a given list
def word_has_character(word, character_list):
    for char in word:
        if char in character_list:
            return True
    return False

# Function to calculate complexity score of a word
def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# Function to calculate password strength
def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("\033[91mPassword is a dictionary word and is not secure.\033[0m")
        return 0
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("\033[91mPassword is a commonly used password and is not secure.\033[0m")
        return 0
    if len(password) < min_length:
        print("\033[91mPassword is too short and is not secure.\033[0m")
        return 1
    if len(password) >= strong_length:
        print("\033[92mPassword is long, length trumps complexity this is a good password.\033[0m")
        return 5
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

# Main function for user interaction
def main():
    print("Welcome to the Password Strength Checker!")
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == "q":
            print("Goodbye!")
            break
        strength = password_strength(password)
        print(f"Password Strength: {strength}/5\n")

if __name__ == "__main__":
    main()