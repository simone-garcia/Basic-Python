#Loop through a range of numbers (1 through 20). This will be up to, but not including 21. 
for x in range(1, 21):
    print(x)

print("***********************************")

#Iterate through letters in a string: 
word = "Supercalifragilisticexpialidocious"
for letters in word:
    print(letters)

print("***********************************")

#Iterate through a list:
groceries = ["Milk", "Eggs", "Cheese", "Toilet Paper", "Dish Detergent"]
print("What did I need from the store again?")
for grocery in groceries:
    print(grocery)

print("***********************************")

#Looping with an condition:
spongebob_reference = "yes"

while spongebob_reference == "yes":
    first = input("Wanna see me run to that mountain and back?")
    if first == "yes":
    spongebob_reference = input("Wanna see me do it again? ")


