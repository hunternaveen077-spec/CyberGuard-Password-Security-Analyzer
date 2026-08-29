import re


def analyze_password(password):
    score = 0
    feedback = []

    # Password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use a longer password.")

    # Uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    # Lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add a number.")

    # Special character
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    # Password strength
    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score, feedback


print("=" * 45)
print("        CYBERGUARD")
print("   Password Security Analyzer")
print("=" * 45)

password = input("Enter a test password: ")

strength, score, feedback = analyze_password(password)

print("\nSecurity Analysis")
print("-" * 25)
print("Strength :", strength)
print("Score    :", str(score) + "/6")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
else:
    print("\nAll basic security checks passed!")

print("\nNote: This tool performs basic local checks.")
