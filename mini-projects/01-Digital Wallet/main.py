def digital_wallet():
    print("=== DIGITAL WALLET ===")
    balance = 0
    history = []

    while True:
        print("1. Check Balance | 2. Deposit | 3. Withdraw | 4. Transaction History | 5. Exit\n")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
                print(f"Your current balance: ${balance:,}")

        elif choice == "2":
            deposit_amount = float(input("Enter deposit amount: $"))

            if deposit_amount > 0:
                balance += deposit_amount
                history.append(f'Deposit : +${deposit_amount:,.2f}')
                print(f"Deposit successful! Your current balance: ${balance:,}")

            else:
                print("Failed: Deposit amount must be greater than $0!")

        elif choice == "3":
            withdraw_amount = float(input("Enter withdrawal amount: $"))

            if withdraw_amount <= 0:
                print("Failed: Amount must be greater than $0!")

            elif withdraw_amount > balance:
                print("Failed: Insufficient funds!")

            else:
                balance -= withdraw_amount
                history.append(f'Withdraw : -${withdraw_amount:,.2f}')
                print(f"Withdrawal successful! Your current balance: ${balance:,}")

        elif choice == "4":
            print('=== Transction History ===')

            if not history:
                print('No transactions yet.')

            else:
                for idx, tx in enumerate(history,1):
                    print(f'{idx}. {tx}')

        elif choice == "5":
            print("Thank you and goodbye!")

            break
        else:
            print("Invalid option! Please choose between 1 and 4.")

# Ask to continue
        if choice in ["1", "2", "3", "4"]:
            continue_tx = (input("\nWould you like to make another transaction? (y/n): ").strip().lower())

        if continue_tx != "y":
            print("Thank you and goodbye!")
            break

digital_wallet()