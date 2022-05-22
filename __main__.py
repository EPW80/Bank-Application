def file_read(UserInformation):
    # fileRead = open(UserInformation.txt, 'r')
    # file name comes as a parameter to the function
    # use that parameter to open the file
    fileRead = open(UserInformation, 'r')
    # lines = fileRead.readline()
    # 'readline' reads one line at a time
    # to rad all lines in a list method is 'readlines'
    lines = fileRead.readlines()
    userNameList = []
    passwordList = []
    balanceList = []
    for i in lines:
        list = i.strip().split()
        userNameList.append(list[0])
        passwordList.append(list[1])
        balanceList.append(list[2])
    return userNameList, passwordList, balanceList


def deposit(balanceList, index):
    amount = int(input("Please enter your deposit amount: "))
    balance = int(balanceList[index])
    new_balance = amount + balance
    balanceList[index] = str(new_balance)
    print("You've made a successful deposit! ")


def withdraw(balanceList, index):
    amount = int(input("Please enter the amount you want to withdraw: "))
    balance = int(balanceList[index])
    if amount > balance:
        print("We're sorry, you do not have the funds to withdraw. Please try again.")
    else:
        new_balance = balance - amount
        balanceList[index] = str(new_balance)
        print("Your transaction was successful. ")


def display_balance(userNameList, balanceList, index):
    # use print with no word separator
    print(userNameList[index], "'s current balance is: ", int(balanceList[index]), sep='')


def changeUser(userNameList, passwordList, balanceList):
    # if user inputs an invalid username
    # it hits the first else statement
    # and index is not set which throws an error on second if
    # so use a 'continue' statement on the first else statement
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
    # use loop to iterate over the lists
    # and write to file
    for i in range(0, len(userNameList)):
        # newline character is '\n', not '/n'
        string = userNameList[i] + " " + \
                 passwordList[i] + " " + balanceList[i] + "\n"

        fileWrite.writelines(string)

    fileWrite.close()
    # return last index as new user is added at the last
    return i


if __name__ == "__main__":
    userNameList, passwordList, balanceList = file_read("UserInformation.txt")
    ################################
    # For better functionality and
    # also for adding new user to the system
    # added a second loop
    ################################
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
            index = add_user("UserInformation.txt", userNameList, passwordList, balanceList)
            break
        elif userInput[0] == 'E':
            exit(1)
        else:
            print("Error! Please enter a valid choice ")

    while True:
        print("D: Deposit money: ")
        print("W: Withdraw money: ")
        print("B: Current balance: ")
        print("C: Change user, display user name: ")
        print("E: Exit program")
        userInput = input("Please enter your choice: ")
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
            add_user("UserInformation.txt", userNameList, passwordList, balanceList)
            print("Bye!")
            break
        else:
            print("Error! Please enter a valid choice ")
