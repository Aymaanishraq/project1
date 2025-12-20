print("Welcome to our Chatbot")
print("What is your name?")
name=input()
print("How are you good or bad ?",name)
answer=input().lower()
if answer=="good":
    print("Having a nice day")
elif answer=="bad":
    print("Really sorry to here that")
else:
    print("Ok don't worry")
print("Ok good bye")
