balance = 1000
transactions = []



def register_transaction(type, amount, old_balance, new_balance, transactions):
    new_transaction = {
        "type": type,
        "amount": amount,
        "old_balance": old_balance,
        "new_balance": new_balance
    }
    transactions.append(new_transaction)


def check_balance(balance):
    print(f"You have ${balance} on your account.")


def deposit(user_balance):
    print("For returning to the main menu: X")
    while True:
        try:
            amount = input("Enter much would you like to deposit: ")

            if amount == "X":
                return user_balance

            if not amount.isdigit():
                print("Deposit amount must be a number")
                raise ValueError("Deposit amount must be a number")
            amount = float(amount)

            if amount <= 0:
                print("Deposit amount has to be a positive number")
                raise ValueError("Deposit amount has to be a positive number")

            new_balance = user_balance + amount
            register_transaction("deposit", amount, user_balance, new_balance, transactions)
            return new_balance
        except:
            pass

def withdraw(user_balance):
    while True:
        try:
            amount = input("Enter withdraw amount: ")

            if amount == "X":
                return user_balance

            if not amount.isdigit():
                print("Deposit amount must be a number")
                raise ValueError("Deposit amount must be a number")
            amount = float(amount)

            if amount <= 0:
                print("Deposit amount has to be a positive number")
                raise ValueError("Deposit amount has to be a positive number")
            

            if amount > user_balance:
                print("Not enough balance on account in order to complete the withdrawal request")
                raise("Not enough balance on account in order to complete the withdrawal request")

            new_balance = user_balance - amount
            register_transaction("withdraw", amount, user_balance, new_balance, transactions)
            return new_balance
        except: 
            pass


def display_transactions(transactions):
    while len(transactions) > 5:
        transactions[1:]
    print(transactions)

def main(balance, transactions):
    while True:
        try:
            print("Welcome ATM!")

            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Last 5 transactions")
            print("5. Exit the ATM")
            
            option = input("Pick operation (1-5): ")

            if not option.isdigit():
                print("Must enter a valid number")
                raise ValueError("Must enter a valid operation number")
            
            option = int(option)

            if option == 1:
                check_balance(balance)
            elif option == 2:
                new_balance = deposit(balance, transactions)
                balance = new_balance
                check_balance(balance)
            elif option == 3:
                new_balance = withdraw(balance, transactions)
                balance = new_balance
                check_balance(balance)
            elif option == 4:
                display_transactions(transactions)
            elif option == 5:
                print("Thank you for using our services")
                print("Quiting program, system shutting down")
                return
            else:
                print("Invalid operation. The command doesn't exist")
                raise ValueError("Invalid operation. The command doesn't exist")
        except:
            pass

main(balance, transactions)