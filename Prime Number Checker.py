print("Prime Number Checker")
#functions
def factors(num):
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list
def prime_num(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime():
    while True:
        #if statements
        integer= int(input("Please enter an integer between 1 and 5000:"))
        if 1 <= integer <= 5000:
            if prime_num(integer):
                print(integer,"is a prime number")
            else:
                factor_list = factors(integer)
                print(integer,"is NOT a prime number")
                print("It has",len(factor_list),"factors",":",factor_list)
        choice = input("Try again? (y/n): ")
        if choice.lower() != 'y':
            break
if __name__ == "__main__":
    prime()

