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
                print("Error! Please enter valid username and/or password")

        else:
            print("Error! Please enter valid username and/or password")
            

