from modules.module_a import sum_values, multiply_values

def main():
    print("Hello World!")
    a = 3
    b = 5

    c = sum_values(a, b)
    d = multiply_values(a, b)

    print(f"The sum of {a} and {b} is {c}")
    print(f"The multiplication of {a} and {b} is {d}")

if __name__ == "__main__":
    main()