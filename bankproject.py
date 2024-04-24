def withdraw(account, amount):
    if amount > account['balance']:
        print("Insufficient funds!")
    else:
        account['balance'] -= amount
        account['transactions'].append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

def deposit(account, amount):
    account['balance'] += amount
    account['transactions'].append(f"Deposit: ${amount}")
    print(f"Deposit successful. Remaining balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def get_transaction_history(account):
    return account['transactions']
flag=0
details={"sonali.sm@gmail.com":123456,
         "shalu.jha@gmail.com":678910,
         "Anju.pai@gmail.com":135790
         }
user=input("Enter username:")
password=int(input("Enter your password"))
c=0
for i in details:
    if(user==i):
        if(password==details[i]):
            print("LOGIN SUCCESS")
            flag=1
            # Create an account dictionary
            account = {
                        'balance': 1000,
                        'transactions': []
                    }

# Dictionary to map user choices to functions
            choices = {
                        '1': deposit,
                        '2': withdraw,
                        '3': get_balance,
                        '4': get_transaction_history
                        }

            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Transaction History")
                print("5. Exit")

                choice = input("Enter your choice: ")

                if choice == '5':
                    print("Exiting program.")
                    break

                if choice in choices:
                    if choice == '1' or choice == '2':
                        c=c+1
                        print(c)
                        if(c>5):
                            print("MAX limit")
                            break
                        else:
                           amount = float(input("Enter amount: "))
                           choices[choice](account, amount)
                    else:
                        print(choices[choice](account))
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("incorrect password")
            flag=1
if(flag==0):
    print("Email not registered,please register")
    
            
        