# Programmer: Erik Williams
# Description: write a program called BankApp to simulate a banking application. The program will
# ask the user to enter username and password. The program will then allow the user to display, add username, deposit
# and withdraw from their account. The program will also update the UserInformation.txt file with new information.
# Date: 5/24/2022

def file_read(UserInformation):
    # use that parameter to open the file
    fileRead = open(UserInformation, 'r')
    lines = fileRead.readlines()  # 'readline' reads one line at a time
    userNameList = []  # initialize variables as empty lists
    passwordList = []
    balanceList = []
    for i in lines:  # iterate thru list appending data
        list = i.strip().split()  # remove empty lines and split string into list
        userNameList.append(list[0])
        passwordList.append(list[1])
        balanceList.append(list[2])
    return userNameList, passwordList, balanceList  # return data to user

def deposit(balanceList, index):  # deposit function
    amount = int(input("Please enter your deposit amount: "))
    balance = int(balanceList[index])  # display balance
    new_balance = amount + balance  # new balance calculation
    balanceList[index] = str(new_balance)  # deposit has been made
    print("You've made a successful deposit! ")  # display to user

def withdraw(balanceList, index):  # withdraw function
    amount = int(input("Please enter the amount you want to withdraw: "))
    balance = int(balanceList[index])  # withdraw has been made
    if amount > balance:  # conditional
        print("We're sorry, you do not have the funds to withdraw. Please try again.")  # display to user
    else:  # otherwise
        new_balance = balance - amount  # new balance calculation
        balanceList[index] = str(new_balance)  # withdraw has been made
        print("Your transaction was successful. ")  # display to user

def display_balance(userNameList, balanceList, index):  # function for account balance
    print(userNameList[index], "'s current balance is: ", int(balanceList[index]), sep='')  # display balance to user

def changeUser(userNameList, passwordList, balanceList):
    # if user inputs an invalid username
    # it hits the first else statement
    # and index is not set which throws an error on second
    # use a 'continue' statement on the first else statement
    # to loop through if an invalid username is entered
    # which avoids the remaining code inside the loop
    while True:
        userName = input("Please enter your username: ")
        passWord = input("Please enter your password: ")
        if userName in userNameList:
            index = userNameList.index(userName)
        else:
            print("Error! Please enter a valid username and/or password")
            continue
        if passWord == passwordList[index]:
            return index
        else:
            print("Error! Please enter a valid username and/or password")

def add_user(UserInformation, userNameList, passwordList, balanceList):
    # same as 'file_read' function
    # file name comes as a parameter to the function
    # use that parameter to open the file
    fileWrite = open(UserInformation, 'w')
    # loop to iterate over the lists
    # and write to file
    for i in range(0, len(userNameList)):
        string = userNameList[i] + " " + passwordList[i] + " " + balanceList[i] + "\n"

        fileWrite.writelines(string)

    fileWrite.close()
    # return last index as new user is added at the last
    return i


if __name__ == "__main__":
    userNameList, passwordList, balanceList = file_read("UserInformation.txt")
    # For better functionality and 
    # also for adding new user to the system
    # added a second loop
    while True:
        print("L: Login")
        print("A: Add new client information")
        print("E: Exit program")
        userInput = input("Please enter your choice: ")
        if(userInput[0] == 'L'):
            index = changeUser(userNameList, passwordList, balanceList)
            break
        elif(userInput[0] == 'A'):
            # input new user information
            userNameList.append(input("Please enter user name: "))
            passwordList.append(input("Please enter your password: "))
            balanceList.append(input("Please enter initial balance: "))
            # write information to file and login
            index = add_user("UserInformation.txt", userNameList, passwordList, balanceList)
            break
        elif(userInput[0] == 'E'):
            exit(1)
        else:
            print("Error! Please enter a valid choice ")

    while True:  # display options to user
        print("D: Deposit money: ")
        print("W: Withdraw money: ")
        print("B: Current balance: ")
        print("C: Change user, display user name: ")
        print("E: Exit program")
        userInput = input("Please enter your choice: ")
        if(userInput[0] == 'D'):
            deposit(balanceList, index)
        elif(userInput[0] == 'W'):
            withdraw(balanceList, index)
        elif(userInput[0] == 'B'):
            display_balance(userNameList, balanceList, index)
        elif(userInput[0] == 'C'):
            index = changeUser(userNameList, passwordList, balanceList)
        elif(userInput[0] == 'E'):
            # write modified information once
            add_user("UserInformation.txt", userNameList, passwordList, balanceList)            
            print("Bye!")
            break
        else:
            print("Error! Please enter a valid choice ")
