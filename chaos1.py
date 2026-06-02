def main():
    print("This program illustrates a chaotic function")

    x = float(input("Enter a number between 0 and 1: "))

    for i in range(30):
        x = 0.5 * x * (1 - x)
        print(x)

main()
