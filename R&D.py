class magicalprime:
    def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

    def reverse_number(n):
        return int(str(n)[::-1])

    def is_magical_prime(n):
        if is_prime(n):
            reversed_n = reverse_number(n)
            return is_prime(reversed_n)
        return False

    num = int(input("Enter a number to check if it's a magical prime: "))
    if is_magical_prime(num):
        print(num, "is a magical prime.")
    else:
        print(num, "is not a magical prime.")
class neon(magicalprime):
    def is_neon_number(num):
        square = num * num
        digit_sum = sum(int(digit) for digit in str(square))
        return digit_sum == num

    def display_neon_numbers(start, end):
        neon_numbers = [num for num in range(start, end + 1) if is_neon_number(num)]
        print("Neon numbers between", start, "and", end, "are:", neon_numbers)

#start_num = int(input("Enter the starting number: "))
#end_num = int(input("Enter the ending number: "))

#display_neon_numbers(1,10)
class X_format(magicalprime):
    def display_name_in_x_pattern(name):
    n = len(name)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print(name[i], end=" ")
            else:
                print(" ", end=" ")
        print()
#name="SONALI"
#display_name_in_x_pattern(name)
class rev(magicalprime):
    def reverse():
        st="SONALI"
        print(st[::-1])

class Banking(neon,X_format):
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
ob1=Banking()
ob2=rev()
ob1.reverse()       
                
