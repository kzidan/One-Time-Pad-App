# Socket is the library being used for messaging
import socket
import qrandom
import math

def decimalToBinary(n):
    return bin(n).replace("0b", "")


def text2binary(userText):
    binaryText = ""
    for chr in userText:
        decimalValue = ord(chr)
        binaryValue = decimalToBinary(decimalValue)
        paddedBinary = str(binaryValue).rjust(7, '0')
        binaryText = binaryText + paddedBinary + " "
    return binaryText

def keyGeneration():
    for i in range (4):
        #Generates random number
        randomNum = qrandom.random()
        #converts from decimal to int
        randomNum = randomNum * 10000000000000000
        randomNum = int(randomNum)
        randomNum = str(randomNum)
        randomNum = text2binary(randomNum)
        print(randomNum, end = "")


def encryption():
    userText = input("Please enter the text you would like to encrypt: ")
    userKey = input("Please enter the key you are using: ")
    # Converts text to binary
    userText = text2binary(userText)
    if len(userText) <= len(userKey):
        print(userText)
        encrypted = ""
        spaceCounter = 0
        for i in range(len(userText)):
            spaceCounter = spaceCounter + 1
            if spaceCounter == 8:
                encrypted = encrypted[:i] + " " + encrypted[i:]
                spaceCounter = 0
            else:
                currText = userText[i]
                currKey = userKey[i]
                currEncrypted = int(currText) ^ int(currKey)
                encrypted = encrypted + str(currEncrypted)
        print("Your encrypted text is: " + encrypted)
    else:
        print("Sorry, your text is longer than your key")


def decryption():
    userText = input("Please enter the text you would like to decrypt: ")
    userKey = input("Please enter the key you are using: ")
    decrypted = ""
    spaceCounter = 0
    for i in range(len(userText)):
        spaceCounter = spaceCounter + 1
        if spaceCounter == 8:
            spaceCounter = 0
        else:
            currEncrypted = userText[i]
            currKey = userKey[i]
            currDecrypted = int(currEncrypted) ^ int(currKey)
            decrypted = decrypted + str(currDecrypted)

    print(decrypted)
    spaceCounter = 0
    for i in range(len(decrypted)):
        spaceCounter = spaceCounter + 1
        if spaceCounter == 8:
            decrypted = decrypted[:i] + " " + decrypted[i:]
            spaceCounter = 0
    decryptedConversion = decrypted.split(" ")
    decryptedText = ""
    for decryptedByte in decryptedConversion:
        decimalValue = int(decryptedByte, 2)
        characterValue = chr(decimalValue)
        decryptedText = decryptedText + characterValue
    print("Your decrypted text is: " + decryptedText)

def sendMessage():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 9999))
    server.listen()
    client, addr = server.accept()
    client.send(input("Message: ").encode('utf-8'))

def recieveMessage():
    #This is the messaging portion of the app
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 9999))
    message = client.recv(1024).decode('utf-8')
    print(message)

userChoice = 0
print("*****************************")
print("PLEASE READ BEFORE PROCEEDING")
print("*****************************")
print("This app provides a way for you to share messages using a OTP (One Time Pad)")
print("The One Time Pad provides you with perfect secrecy, to take advantage of this you")
print("must follow a few rules:")
print("Never reuse a key, reusing a key will break perfect secrecy")
print("Store your key in a safe location, if your key is compromised so is perfect secrecy")
print("Your key must be larger than or equal to the message you are sending")
print("Please use a truly random method to generate your key, such as our built in function")
print("Thank you")
while userChoice != 6:
    print("")
    print("1) Generate a Key")
    print("2) Encrypt a message")
    print("3) Decrypt a message")
    print("4) Send a message")
    print("5) Recieve a message")
    print("6) End the program")
    userChoice = int(input("Please enter a choice: "))
    if userChoice == 1:
        keyGeneration()
    elif userChoice == 2:
        encryption()
    elif userChoice == 3:
        decryption()
    elif userChoice == 4:
        sendMessage()
    elif userChoice == 5:
        recieveMessage()