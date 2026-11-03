print("Think of a number from 1 to 100")

low = 1
high = 100

while low <= high:
    guess = (low + high) // 2
    print("My guess is:", guess)

    answer = input("Higher, Lower or Correct? ").lower()

    if answer == "higher":
        low = guess + 1

    elif answer == "lower":
        high = guess - 1

    elif answer == "correct":
        print("Number guessed successfully!")
        break

    else:
        print("Invalid answer!")

if low > high:
    print("No matching number found!")
