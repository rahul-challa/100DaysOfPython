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

def code(message):
    if (len(message) >= 3):
        print(frontRandomLetters + message[1:] + message[0] + backRandomLetters)
    else:
        print(message[::-1])

def decode(message):
    if (len(message) > 3):
        print(message[::-1])
    else:
        print(message[-4] + message[3:-4])

print("--------------------------------------------------------------------------------------------")
message = (input("Enter your Message here: "))
print(f"the message you entered is: \"{message}\"\n")
print("Enter \"code\" to code this message.\n")
print("Enter \"decode\" to decode this message.\n")
choice = input("Enter your choice: \n")
frontRandomLetters = "isd"
backRandomLetters = "ner"

if(choice == "code"):
    print(code(message))
elif(choice == "decode"):
    print(code(message))