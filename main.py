#this is the main code of the bot
import os 
from learner import info

def learn(quality):
    if quality=="fine":
        fine = True
    else:
        fine = False
    print(fine ,"🥰")

input("Press any bottom")

condn = input("hi, how are you?")
if condn=="fine":
    print("Good to here that..!")
else:
    print("Sorry to hear that but I believe that you are gonna make it..!")
learn(condn)
print("This following code is to check that the terminal has in built abilities to compile the code")
info()