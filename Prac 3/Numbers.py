def main():
    numbers = []
    amount = int(input("You will be entering 5 numbers. Let's clarify - how many numbers will you enter?"))

    for number in range(1, amount + 1):
        number = (input("Enter your first number " + str(number) + ": "))
        numbers.append(number)

    print("Your first number is " + (numbers[0]))
    print("Your first number is " + (numbers[4]))
    print("Your smallest number is " + min(numbers))
    print("Your largest number is " + max(numbers))

main()

