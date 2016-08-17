name = input("Please enter your name")

while name == "" or name == " ":
    name = input("Please enter your name")

for i in range(1, len(name), 2):
    print(name[i])