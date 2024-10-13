import random
def roll_die():
    return random.randint(1,6)
def main():
    while True:
        print("Dice Roller")

        Die1 = roll_die()
        Die2 = roll_die()

        Total = Die1 + Die2

        print(f"Die 1: {Die1}", f"\nDie 2: {Die2}")
        print("Total:", Total)

        if Total == 2:
            print("Snake eyes!")
        elif Total == 12:
            print("Boxcars!")
        choice = input("Roll again (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()







