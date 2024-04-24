username="sonali.am24@gmail.com"
user=str(input("Enter your email id"))
pwd=str(input("Enter the password"))
if(user==username):
    if(pwd=="123login"):
        print("Login success")
        OTP=1234
        OTPU=int(input("Enter the otp"))
        if(OTPU==OTP):
            print("Transaction successful")
        else:
            print("Transaction failed incorrect otp")
    else:
        print("Login failed due to incorrect email")

else:
    print("Login failed due to incorrect email")
    
