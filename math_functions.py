def add(x: float, y: float) -> float:
    return x + y

def multiply(x: float, y: float) -> float:
    return x * y

def square(x: float) -> float:
    return multiply(x, x)

def add_squares(x: float, y: float) -> float:
    return add(square(x), square(y))

def main():
    sum_of_nums = add(5, 10)
    print(sum_of_nums)

    multiplication = multiply(5, 100)
    print(multiplication)

    square_of_nums = square(8)
    print(square_of_nums)

    add_square_nums = add_squares(10, 100)
    print(add_square_nums)

if __name__ == "__main__":
    main()
