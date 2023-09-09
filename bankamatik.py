medusa = {

    "account_no":"10050",
    "full_name": "irem",
    "user_name":"medusa",
    "password":"123",
    "balance":3000,
    "additional_balance":1000
    
   
}
maestro = {

    "account_no":"150223",
    "full_name": "berk",
    "user_name":"maestro",
    "password":"123",
    "balance":5000,
    "additional_balance":1000
    
   
}

users = [medusa,maestro]
 
def withdraw_money(account:dict,amount:int):
    if account["balance"] >= amount:
        account["balance"] -= amount
        print("dont forget to take your money..!")
        balance_result(account)
    else:
        total_balance = account["balance"] + account['additional_balance']

        if total_balance>=amount:
            use_additional_balance=input("insufficent balance. use additional balance?")
            if use_additional_balance=="yes":
                 amount_used_additional_account = amount - account["balance"]
                 account["balance"] = 0
                 account["additional balance"] -= amount_used_additional_account
                 balance_result(account)
            elif use_additional_balance== "no":
                print("process has been cancaled")
                balance_result(account)
            else:
                 print("please enter yes or no")
        else:
             print("insufficent total balance. Transaction cancaled")
             balance_result(account)

def balance_result(account: dict) -> None:
	print(f"You have {account['balance']} TL account number {account['account_no']}.\n Additional balance has {account['additional_balance']} TL.")
        

def show_account_information(account:dict):
     print(f"account information\n"
           f"name:{account['full_name']}\n"
           f"account:{account['account_no']}\n"
           f"user name:{account['user_name']}\n"
           f"password:{account['password']}\n"
           f"balance:{account['balance']}\n"
           f"additional balance:{account['additional_balance']}"
     
     )
def deposit_money(account: dict, amount: int):
    account["balance"] += amount
    print(f"{amount} TL successfully credited to your account.")
    balance_result(account)

def user_login(username: str, password: str):
    for user in users:
        if user['user_name'] == username and user['password'] == password:
            return user
    print("Username or password is incorrect.")
    return None

def main():
    while True:
        username = input("Enter your username: ")
        password = input("enter your password: ")
        user = user_login(username, password)
        if user is not None:
            while True:
                print("\n1. View Account Information")
                print("2. Withdraw Money")
                print("3. Deposit Money")
                print("4. Log Out")
                choice = input("\nMake your choice: ")
                if choice == '1':
                    show_account_information(user)
                elif choice == '2':
                    amount = int(input("\nenter the withdrawal amount you want: "))
                    withdraw_money(user, amount)
                elif choice == '3':
                    amount = int(input("\nEnter the amount you want to deposit: "))
                    deposit_money(user, amount)
                elif choice == '4':
                    print("\nThe exit has been made.")
                    break
                else:
                    print("\nInvalid election. Please try again.")
            if choice == '4':
                break
        else:
            print("\nInvalid username or password. Please try again.")
main()


     
     