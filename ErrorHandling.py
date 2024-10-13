try:
    number = int(input("Enter Integer: "))
    print(f"You've entered a valid integer f {number}.")
except ValueError:
    print(f"You've entered an invalid integer f {number}.")


print("Thanks")