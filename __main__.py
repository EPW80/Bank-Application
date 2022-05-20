def file_read(UserInformation):
    fileRead = open(UserInformation.txt, 'r')
    lines = fileRead.readline()
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
    print(userNameList[index], "'s current balance is: ",
          int(balanceList[index]))


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


def add_user(UserInformation, userNameList, passwordList, balanceList):
    fileWrite = open(UserInformation.txt, 'w')
    string1 = userNameList[0] + " " + \
        passwordList[0] + " " + balanceList[0] + "/n"
    fileWrite.writelines(string1)
    string1 = userNameList[1] + " " + \
        passwordList[1] + " " + balanceList[1] + "/n"
    fileWrite.writelines(string1)
    string1 = userNameList[2] + " " + \
        passwordList[2] + " " + balanceList[2] + "/n"
    fileWrite.writelines(string1)
    fileWrite.close()


if __name__ == "__main__":
    userNameList, passwordList, balanceList = file_read("UserInformation.txt")

    index = changeUser(userNameList, passwordList, balanceList)
    while True:
        print("D: Deposit money: ")
        print("W: Withdraw money: ")
        print("B: Current balance: ")
        print("C: Change user, display user name: ")
        print("A: Add new client information:")
        print("E: Exit program")

        userInput = input("Please enter your choice: ")
        if(userInput[0] == 'D'):
            deposit(balanceList, index)
            add_user("UserInformation.txt", userNameList,
                     passwordList, balanceList)
        elif(userInput[0] == 'W'):

            withdraw(balanceList, index)
            add_user("UserInformation.txt",  userNameList,
                     passwordList, balanceList)
        elif(userInput[0] == 'B'):
            display_balance(userNameList, balanceList, index)

        elif(userInput[0] == 'C'):

            index = changeUser(userNameList, passwordList, balanceList)

        elif(userInput[0] == 'A'):

            index = add_user(userNameList, passwordList, balanceList)

        elif(userInput[0] == 'E'):
            print("Bye! ")
            break

        else:
            print("Error! Please enter a valid choice ")
