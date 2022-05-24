# Programmer: Erik Williams
# Description: write a program called BankApp to simulate a banking application. The program will
# ask the user to enter username and password. The program will then allow the user to display, add username, deposit
# and withdraw from their account. The program will also update the UserInformation.txt file with new information.
# Date: 5/24/2022

def file_read(UserInformation):  # fileRead = open(UserInformation.txt, 'r')
    fileRead = open(UserInformation, 'r')  # parameter to open the file
    lines = fileRead.readlines()  # 'readline' reads one line at a time
    # initialize variables as empty lists
    userNameList = []
    passwordList = []
    balanceList = []
    for i in lines:  # iterate thru list appending data
        list = i.strip().split()  # remove empty lines and split string into list
        userNameList.append(list[0])
        passwordList.append(list[1])
        balanceList.append(list[2])
    return userNameList, passwordList, balanceList  # return data to user


def deposit(balanceList, index):  # deposit function
    # take user input
    amount = int(input("Please enter your deposit amount: "))
    balance = int(balanceList[index])  # dipskay balance
    new_balance = amount + balance  # new balance calculation
    balanceList[index] = str(new_balance)  # deposit has been made
    print("You've made a successful deposit! ")  # display to user


def withdraw(balanceList, index):  # withdraw function
    # take user input
    amount = int(input("Please enter the amount you want to withdraw: "))
    balance = int(balanceList[index])  # withdraw has been made
    if amount > balance:  # conditional
        # display to user
        print("We're sorry, you do not have the funds to withdraw. Please try again.")
    else:  # otherwise
        new_balance = balance - amount  # new balance calculation
        balanceList[index] = str(new_balance)  # withdraw has been made
        print("Your transaction was successful. ")  # display to user


def display_balance(userNameList, balanceList, index):  # function for account balance
    print(userNameList[index], "'s current balance is: ",  # print to user
          int(balanceList[index]), sep='')  # display balance


def changeUser(userNameList, passwordList, balanceList):

    while True:  # while statement
        userName = input("Please enter your username: ")
        passWord = input("Please enter your password: ")
        if userName in userNameList:  # if username is correct
            index = userNameList.index(userName)  # accept user
        else:  # otherwise
            print("Error! Please enter a valid username and/or password")
            continue  # a 'continue' statement on the first else statement
        # loop through if an invalid username is entered
        if passWord == passwordList[index]:
            return index  # print data to user
        else:  # otherwise
            # display to user
            print("Error! Please enter a valid username and/or password")


def add_user(UserInformation, userNameList, passwordList, balanceList):  # same as 'file_read' function
    # file name comes as a parameter to the function
    fileWrite = open(UserInformation, 'w')  # parameter to open the file
    # use loop to iterate over the lists
    # and write to file
    for i in range(0, len(userNameList)):  # iterate thru list 
        string = userNameList[i] + " " + \
            passwordList[i] + " " + balanceList[i] + "\n"  # data is locked in

        fileWrite.writelines(string)  # write string to .txt file

    fileWrite.close()  # close file

    return i  # return last index as new user is added at the last


if __name__ == "__main__":
    userNameList, passwordList, balanceList = file_read("UserInformation.txt")
   
   
    while True:
        print("L: Login")
        print("A: Add new client information")
        print("E: Exit program")
        userInput = input("Please enter your choice: ")
        if userInput[0] == 'L':
            index = changeUser(userNameList, passwordList, balanceList)
            break
        elif userInput[0] == 'A':
            # input new user information
            userNameList.append(input("Please enter user name: "))
            passwordList.append(input("Please enter your password: "))
            balanceList.append(input("Please enter initial balance: "))
            # write information to file and login
            index = add_user("UserInformation.txt",
                             userNameList, passwordList, balanceList)
            break
        elif userInput[0] == 'E':
            exit(1)
        else:
            print("Error! Please enter a valid choice ")
    # second loop for better performance
    while True:
        # priint to user
        print("D: Deposit money: ")
        print("W: Withdraw money: ")
        print("B: Current balance: ")
        print("C: Change user, display user name: ")
        print("E: Exit program")
        userInput = input("Please enter your choice: ")  # take user input
        # select from list of options
        if userInput[0] == 'D':
            deposit(balanceList, index)
        elif userInput[0] == 'W':
            withdraw(balanceList, index)
        elif userInput[0] == 'B':
            display_balance(userNameList, balanceList, index)
        elif userInput[0] == 'C':
            index = changeUser(userNameList, passwordList, balanceList)
        elif userInput[0] == 'E':
            # write modified information once
            add_user("UserInformation.txt", userNameList,
                     passwordList, balanceList)
            print("Bye!")
            break  # end if
        else:  # otherwise display error
            print("Error! Please enter a valid choice ")
