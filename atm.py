import time
print("================")
print("Insert Your CARD")
print("================")
time.sleep(1)
password= 1234
pin= int(input("Enter Your PIN:"))
balance = 5000


if pin == password:
    while True:
            print("""
             ***********************
                1 == balance
                2 == withdraw_balance
                3 == deposit_balance
                4 == exit
              """)
            try:
                option = int(input("Please Select Your Choise: "))
            except:
                 print("please enter valid option")

            if option == 1:
                 print(f"Your current balance is {balance}")
                 break

            if option == 2:
                 withdraw_amount = int(input("Please enter your Withdraw_Amount:"))
                 balance = balance - withdraw_amount
                 print(f"{withdraw_amount} is debited from your account")

                 print(f"Your current balance is {balance}")
                 break

            if option == 3:
                deposit_amount = int(input("please enter deposit amount:"))
                balance = balance + deposit_amount
                print(f"{deposit_amount} is added to your account")
                print(f"your update balance is {balance}")
                break

            if option == 4:
                break

else:
 print("wrong pin try again")