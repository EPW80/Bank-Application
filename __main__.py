from pickletools import string1


def file_read(scores):
    fileRead = open(scores.txt, 'r')
    # fileWrite = open(scoresResults.txt, 'w')
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

def show_balance(userNameList, balanceList, index):
    print(userNameList[index], "'s current balance is: ", int(balanceList[index]))

def update_file(scoresResult, userNameList, passwordList, balanceList):
    fileWrite = open(scoresResult, 'w')
    string1 = userNameList[0] + " " + passwordList[0] + " " + balanceList[0] + "/n"
    fileWrite.writelines(string1)
    string1 = userNameList[1] + " " + passwordList[1] + " " + balanceList[1] + "/n"
    fileWrite.writelines(string1)
    string1 = userNameList[2] + " " + passwordList[2] + " " + balanceList[2] + "/n"
    fileWrite.writelines(string1)
    fileWrite.close()
    