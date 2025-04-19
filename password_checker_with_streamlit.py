import re
import random

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("➔ Make the password at least 8 characters long.")
    
    # Uppercase and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("➔ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("➔ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("➔ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    print("\nPassword Analysis:")
    if score == 4:
        print("✅ Strong Password! Great job!")
    elif score == 3:
        print("⚠️ Moderate Password - Consider improving it:")
        for suggestion in suggestions:
            print(suggestion)
    else:
        print("❌ Weak Password - Needs improvement:")
        for suggestion in suggestions:
            print(suggestion)

def generate_strong_password():
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    special = "!@#$%^&*"
    all_chars = upper + lower + digits + special

    # Ensure at least one of each type
    password = random.choice(upper) + random.choice(lower) + random.choice(digits) + random.choice(special)

    # Add more random characters to make it at least 8-12 characters
    password += ''.join(random.choice(all_chars) for _ in range(random.randint(4, 8)))
    password = ''.join(random.sample(password, len(password)))  # Shuffle the result
    return password

# List of blacklisted common passwords
blacklist = ['password', '123456', 'qwerty', 'password123', 'admin', 'letmein']

def main():
    password = input("🔒 Enter your password: ")

    if password.lower() in blacklist:
        print("\n❌ This password is too common and easily guessable. Please choose a stronger one!")
        print(f"🔹 Suggested Strong Password: {generate_strong_password()}")
    else:
        check_password_strength(password)

        # Suggest a strong password if user's password is weak
        if len(password) < 8 or not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) \
           or not re.search(r"\d", password) or not re.search(r"[!@#$%^&*]", password):
            print(f"\n🔹 Suggested Strong Password: {generate_strong_password()}")

if __name__ == "__main__":
    main()
