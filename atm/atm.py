from cardHolder import cardHolder
def printMenu():
    print("Choose an operation from the following")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show balance")
    print("4. Exit")

###deposit function
def deposit(cardHolder):
    try:

        deposit=float(input("Enter the amount you would like to deposit : "))
        cardHolder.set_balance(cardHolder.get_balance()+ deposit)
        print("your deposit is completed ,your new balance is:", str(cardHolder.get_balance()))
    except:
        print("invalid input")
###withdraw
def withdraw(cardHolder):
    try:
        withdraw=float(input("Enter the amt you want to withdraw: "))
        if (cardHolder.get_balance()<withdraw):
            print("Insufficent balance")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("Your withdraw is completed")
    except:

        print("invalid input")
###show balance
def show_balance(cardHolder):
    print("your current balance :", cardHolder.get_balance())

if __name__=="__main__":
    current_user=cardHolder("","","","","")

### creating repo for cardholders
    list_of_cardHolders=[]
    list_of_cardHolders.append(cardHolder( "5478954781" , 1111, "Amrit" , "Rai" ,654.7))
    list_of_cardHolders.append(cardHolder( "7468512354" , 2222, "Shivam" , "Yadav" ,476.25))
    list_of_cardHolders.append(cardHolder( "9756842369" , 3333, "Rishabh" , "singh" ,546))
    list_of_cardHolders.append(cardHolder( "9745618347" , 4444, "Bilal" , "Mohsin" ,954.22))
    list_of_cardHolders.append(cardHolder( "6479135486" , 5555, "Aman" , "Singh" ,652))
### promt user for debit card no
debitcardNum = ""
while True:
    try:
        debitcardNum=input("input your card no: ")
        debitMatch=[holder for holder in list_of_cardHolders if holder.cardNum == debitcardNum]
        if (len (debitMatch)>0):
            current_user = debitMatch[0]
            break
        else:
            print("Card no not found , please try again")
    except:
        print("Card no not found , please try again")
### prompt user PIN
while True:
    try:
        user_pin = input("Please enter your PIN: ").strip()
        # Convert user input PIN to integer for comparison
        user_pin = int(user_pin)
        
        if current_user.get_pin() == user_pin:
            break
        else:
            print("Invalid PIN, please try again")
    except ValueError:
        print("Invalid PIN format, please enter a numeric PIN.")
    except:
        print("Invalid PIN, please try again")
### printing
print("Welcome",current_user.get_firstName(),".")
option=0
while (True):
    printMenu()  
    try:
        option=int(input())
    except:
        print("Invalid option ,please try again.")
    if (option==1):
        deposit(current_user)
    elif(option==2):
        withdraw(current_user)
    elif(option==3):
        show_balance(current_user)
    elif(option==4):
        break
    else:
        option=0
print("Thank you for using our services.")
