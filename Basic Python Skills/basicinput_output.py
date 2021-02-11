#Collect user's name:
name = input("What is your name? ")
print("Hello " + str(name))

#Collect user's age:
age = int(input("How old are you? "))

#Basic response via condition:
if age < 50:
    print("You still have your entire life ahead of you.")
else:
    print("The things you have seen in this lifetime, am I right? XD")

#Collect user's occupation:
occupation = input("What do you do for a living? ")
print("Working as a " + str(occupation) + " is a noble profession. ")

#Collect user's origin:
origin = input("So where are you from? ")

#Basic response via condition:
if origin == "Nashville":
    print("It is a nice place to call home, isn't it?")
else: 
    print(str(origin) + ", I can't say I've ever been.")

print("Thanks for chatting, I must go now.")




    
