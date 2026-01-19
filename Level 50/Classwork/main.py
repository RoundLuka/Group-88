"""•    საწყისი ბალანსი: 1000 ლარი
•    მთავარი მენიუ (while ციკლით):
ბალანსის შემოწმება
თანხის შეტანა
თანხის გატანა
ბოლო 5 ტრანზაქციის ნახვა
გასვლა
•    ყოველ ოპერაციაზე:
იყენებს try-except ბლოკს:
ValueError - არასწორი რიცხვის შეტანა
არასწორი მენიუს არჩევანი
თანხის გატანისას ამოწმებს საკმარისი ბალანსის არსებობას
შეტანისას და გატანისას ამოწმებს დადებითი რიცხვის შეყვანას
•    ინახავს ტრანზაქციების ისტორიას სიაში: [{'type': 'შეტანა/გატანა', 'amount': თანხა, 'balance': ახალი_ბალანსი}, ...]
•    აჩვენებს ბოლო 5 ტრანზაქციას ფორმატირებული სახით
•    გასვლისას აჩვენებს საბოლოო ბალანსს და ტრანზაქციების რაოდენობას"""

balance = 1000
last_transactions = [
    # {'type': 'შეტანა/გატანა', 'amount': თანხა, 'balance': ახალი_ბალანსი}
]

def add_transaction(type, amount, balance):
    last_transactions.append(
        {
            "type": type, 
            "amount": amount,
            "balance": balance,
        }
    )

def deposit(user_balance):
    amount = 0
    while True:
        try:
            amount = int(input("შეიყვანეთ თანხა: "))
            
            if amount < 0:
                raise ValueError("შემოსატანი თანხის ოდენობა აუცილებლად დადებითი უდნა იყოს")
        except ValueError:
            print("გთხოვთ ჩაწეროთ რიცხვი")
        else:
            break
        
    user_balance += amount
    print(f"თქვენ წარმატებით შეიტანეთ {amount}₾ ანგარიშზე, თქვენი ახალი ბალანსი შეადგენს {user_balance}")
    add_transaction("deposit", amount, user_balance)
    return user_balance

def withdraw(user_balance):
    amount = 0
    while True:
        try:
            amount = int(input("შეიყვანეთ თანხა: "))
            
            if amount < 0:
                raise ValueError("შემოსატანი თანხის ოდენობა აუცილებლად დადებითი უდნა იყოს")
            if amount > user_balance:
                raise ValueError("თქვენ ანგარიშზე საკმარისი თანხა არ არის")
        except ValueError:
            print("გთხოვთ ხელახლა სცადოთ")
        else:
            break
        
    user_balance -= amount
    print(f"თქვენ წარმატებით გაიტანეთ {amount}₾ ანგარიშიდან, თქვენი ახალი ბალანსი შეადგენს {user_balance}")
    add_transaction("withdraw", amount, user_balance)
    return user_balance

def keep_five(all_transactions):
    while len(all_transactions) > 5:
        all_transactions.pop(0)


while True:
    print("Welcome to the ATM")
    print("1. ბალანსის შემოწმება")
    print("2. თანხის შეტანა")
    print("3. თანხის გატანა")
    print("4. ბოლო 5 ტრანზაქციის ნახვა")
    print("5. პროგრამიდან გასვლა")

    while True:
        try:
            operation = int(input("აირჩიეთ ოპერაცია (1-5): "))
        except ValueError:
            print("გთხოვთ შემოიყვანოთ მხოლოდ რიცხვი 1-იდან 5-მდე")
            operation = int(input("აირჩიეთ ოპერაცია (1-5): "))
        else:
            break
    if operation == 1:
        print(f"თქვენი ბალანსია {balance}")
    elif operation == 2:
        new_balance = deposit(balance)
        balance = new_balance
        keep_five(last_transactions)
    elif operation == 3:
        new_balance = withdraw(balance)
        balance = new_balance
        keep_five(last_transactions)
    elif operation == 4:
        print(last_transactions)
    elif operation == 5:
        break
    else:
        print("თქვენ მიერ არჩეული ოპერაციის ნომერი არასწორია, სცადეთ ხელახლა")