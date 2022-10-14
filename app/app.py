from modules.module_a.arithmetic_operations import sum_values, multiply_values
from modules.module_b.identity_operations import identity

def main():
    print("Hello World!")
    a = 3
    b = 5

    c = sum_values(a, b)
    d = multiply_values(a, b)
    e = identity(a)

    print(f"The sum of {a} and {b} is {c}")
    print(f"The multiplication of {a} and {b} is {d}")
    print(f"value {a} is the same as {e}")

if __name__ == "__main__":
    main()