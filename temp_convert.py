# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Nov. 27, 2022
# This program prints converts celsius to fahrenheit in a function


def fahrenheit():
    try:
        celsius = float(input("Enter temperature (°C): "))
    except:
        print("Please enter a valid temperature")
    else:
        fahrenheit = 9 / 5 * celsius + 32
        print(f"{celsius}°C is {fahrenheit:.2f}°F")


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
