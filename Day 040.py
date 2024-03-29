'''
# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
'''
# Function to encrypt
def code(message):
    print("the coded message is:\n")
    if (len(message) >= 3):
        print(frontRandomLetters + message[1:] + message[0] + backRandomLetters)
    else:
        print(message[::-1])

# Function to decrypt
def decode(message):
    print("the decoded message is:\n")
    if (len(message) < 3):
        print(message[::-1])
    else:
        step1 = message[3:len(message)-3]
        step2 = step1[-1] + step1[0:-1]
        print(step2)

print("--------------------------------------------------------------------------------------------")
message = (input("Enter your Message here: \n"))
print(f"the message you entered is: \"{message}\"\n")
print("--------------------------------------------------------------------------------------------")
print("Enter \"code\" to code this message.")
print("Enter \"decode\" to decode this message.")
print("--------------------------------------------------------------------------------------------")
choice = input("Enter your choice: \n")
print("--------------------------------------------------------------------------------------------")
frontRandomLetters = "isd"
backRandomLetters = "ner"

if __name__ == '__main__':
    if(choice == "code"):
        code(message)
    elif(choice == "decode"):
        decode(message)