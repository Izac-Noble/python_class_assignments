
def to_celsius(f):
    c = (f-32) * 5/9
    return c

def to_fahrenhite(c):
    f = c * 9/5 + 32
    return f

def main():
    for temp in range(0,212,40):
        print(temp, "Fahrenhit =", round(to_celsius(temp)),"Celsius")

    for temp in range(0,100,20):
        print(temp, "Celsius =", round(to_fahrenhite(temp)),"Fahrenhite")

if __name__ == "__main__":
    main()