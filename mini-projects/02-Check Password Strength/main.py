def check_password_strength(your_password):
    uppercase = False
    lowercase = False
    numeric = False
    score = 0

    # 1. Check each character
    for char in your_password:
        if char.isupper():
            uppercase = True
        if char.islower():
            lowercase = True
        if char.isdigit():
            numeric = True

    # 2. Display verification status on screen
    print(f"Uppercase : {uppercase}")
    print(f"Lowercase : {lowercase}")
    print(f"Numeric   : {numeric}")

    if len(your_password) >= 8:
        print("Length    : True")
    else:
        print("Length    : False")

    # 3. Calculate score step-by-step
    if uppercase:
        score += 1

    if lowercase:
        score += 1

    if numeric:
        score += 1

    if len(your_password) >= 8:
        score += 1

    print(f"Total Score: {score}/4")

    # 4. Determine strength level
    if score <= 2:
        print("Status    : Password is Weak 🔴 !!")
    elif score == 3:
        print("Status    : Password is Medium 🟡 !!")
    else:
        print("Status    : Password is Strong 🟢 !!")


def main():
    print("=== Welcome to Password Strength Checker ===")
    print("Type 'exit' to quit the program.\n")

    while True:
        your_password = input("Input Your Password: ").strip()

        if your_password.lower() == "exit":
            print("\n=== Program Terminated. Goodbye! ===")
            break

        if your_password == "":
            print("Password cannot be empty!\n")
            continue

        print("\n--- Check Results ---")
        check_password_strength(your_password)
        print("-" * 30 + "\n")


if __name__ == "__main__":
    main()
