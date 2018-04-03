"""Kyle Irving"""

while True:
    try:
        name = str(input("Please enter your name"))
        break
    except ValueError:
        print("Sorry, that name is invalid")
        continue
for i in str(len(name)):
    print (name[::2])
