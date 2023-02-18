'''
Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
'''
import time

timestamp = time.strftime('%H:%M:%S')
print("current time is :",timestamp)
hours = int(time.strftime('%H'))
minutes = int(time.strftime('%M'))
seconds = int(time.strftime('%S'))
if(hours>0 and hours<12):
    print("GOOD MORNING!!!!")
elif(hours<=12 and hours<4):
    print("GOOD AFTERNOON!!!!")
else:
    print("GOOD EVENING!!!!")