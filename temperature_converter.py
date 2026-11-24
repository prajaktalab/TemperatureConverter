
# Temperature Converter

def c_to_f(c):
    return (c * 9/5) + 32


def f_to_c(f):
    return (f - 32) * 5/9


def c_to_k(c):
    return c + 273.15


# Additional feature
def f_to_k(f):
    return (f - 32) * 5/9 + 273.15


def main():
    print("===== TEMPERATURE CONVERTER =====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Fahrenheit to Kelvin")

    choice = int(input("Enter your choice: "))
    temp = float(input("Enter temperature: "))

    if choice == 1:
        print("Temperature in Fahrenheit:", round(c_to_f(temp), 2))
    elif choice == 2:
        print("Temperature in Celsius:", round(f_to_c(temp), 2))
    elif choice == 3:
        print("Temperature in Kelvin:", round(c_to_k(temp), 2))
    elif choice == 4:
        print("Temperature in Kelvin:", round(f_to_k(temp), 2))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
