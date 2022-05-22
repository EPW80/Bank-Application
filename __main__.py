def readFile(fileName):
    file1 = open(fileName, 'r')  # open file in read mode only
    Lines = file1.readlines()  # read every line
    # create lists
    userNameList = []
    passwordList = []
    balanceList = []
    # iterate through each line
    for line in Lines:
        List = line.strip().split()  # space split
        # attach to list
        userNameList.append(List[0])
        passwordList.append(List[1])
        balanceList.append(List[2])

    return userNameList, passwordList, balanceList


def changeUser(userNameList, passwordList, balanceList):
    while True:
        userName = input("Please enter your username: ")
        passWord = input("Please enter your password: ")
        if userName in userNameList:
            index = userNameList.index(userName)
            if passWord == passwordList[index]:
                return index
            else:
                print("Error! Please enter a valid username and/or password")

        else:
            print("Error! Please enter a valid username and/or password")


def deposit(balanceList, index):
    amount = int(input("Please enter your deposit amount: "))
    balance = int(balanceList[index])
    newBalance = amount + balance
    balanceList[index] = str(newBalance)
    print("Your deposit was successful! ")


def withDraw(balanceList, index):
    amount = int(input("Please enter the amount you want to withdraw: "))
    balance = int(balanceList[index])
    if amount > balance:
        print("We're sorry, you do not have the funds to withdraw. Please try again.")
    else:
        newBalance = balance - amount
        balanceList[index] = str(newBalance)
        print("Your transaction was successful. ")


def showBalance(userNameList, balanceList, index):
    print(userNameList[index], "'s current balance is: ", int(balanceList[index]))


def updateFile(fileName, userNameList, passwordList, balanceList):
    file1 = open(fileName, "w")
    str1 = userNameList[0] + " " + passwordList[0] + " " + balanceList[0] + "/n"
    file1.writelines(str1)
    str1 = userNameList[1] + " " + passwordList[1] + " " + balanceList[1] + "/n"
    file1.writelines(str1)
    str1 = userNameList[2] + " " + passwordList[2] + " " + balanceList[2] + "/n"
    file1.writelines(str1)
    file1.close()


if __name__ == "__main__":
    userNameList, passwordList, balanceList = readFile("UserInformation.txt")
    index = changeUser(userNameList, passwordList, balanceList)
    while True:
        print("D: Deposit money: ")
        print("W: Withdraw money: ")
        print("B: Current balance: ")
        print("C: Change user, display user name: ")
        # print("A: Add new client information:")
        print("E: Exit program")
        userInput = input("Please enter your choice: ")
        if userInput[0] == "D":
            deposit(balanceList, index)
            updateFile("UserInformation.txt", userNameList, passwordList, balanceList)
        elif userInput[0] == "W":
            withDraw(balanceList, index)
            updateFile("UserInformation.txt", userNameList, passwordList, balanceList)
        elif userInput[0] == "B":
            showBalance(userNameList, balanceList, index)
        elif userInput[0] == "C":
            index = changeUser(userNameList, passwordList, balanceList)
        # elif userInput[0] == 'A':
        #     index = add_user(userNameList, passwordList, balanceList)
        elif userInput[0] == "E":
            print("Thank you. Have a great day! ")
            break
        else:
            print("Error! Please enter a valid choice ")
