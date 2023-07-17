print("Welcome to a Virtual Credit Union ATM!")
counter = 0
while counter < 3:
    pin = input("Please input your 4-digit PIN: ")
 
    if pin == 9876:
        print("Correct PIN, will continue to menu")
        break
 
    print("Incorrect PIN, please try again")
    counter += 1
 
if counter == 3:
    print("You're locked out, Goodbye")
else:
    print("Onto Menu options")
 
    
while loop:          
    menu()   
    choice = input("Enter your choice [1-4]: ")
 
    if choice == 1:
        account_balance = (int, 'Your account balance is: $500')
        print(account_balance)
 
    elif choice == 2:
        print ("Withdraw Cash, must be multiple of 10")
        withdraw = int(input('How much do you want to Withdraw?:'))
 
        if withdraw > account_balance:
            print("Insufficient funds")
            withdraw = int(input("Enter new amount to Withdraw: "))
 
        elif withdraw <= account_balance:
            balance = account_balance - withdraw
            print (' New Balance :', balance)
 
    elif choice == 3:
        print ("Make Deposit")
        deposit = int(input('How much do you want to Deposit?:'))
        r = input("Are you sure you want to deposit ", deposit, "? [Y/N]")
        if choice == y:
            balance = account_balance + deposit
            print (' New Balance:', balance)
 
        elif choice == n:
            deposit2 = input("Enter the amount you want to deposit")
            balance = account_balance + deposit2
            print (' New Balance:', balance)
 
    elif choice == 4:
        print ("Exit, Goodbye!")
        break
 
        loop = False 
    else:
        raw_input("Wrong option selection. Enter any key to try again..")