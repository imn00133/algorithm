# https://www.acmicpc.net/problem/10872
# Solving Date: 20.03.28.


def recursive_factorial(number):
    if number == 0:
        return 1
    else:
        return number * recursive_factorial(number-1)


def loop_factorial(number):
    factorial = 1
    if number != 0:
        for num in range(1, number+1):
            factorial *= num
    return factorial


def main():
    number = int(input())
    print(recursive_factorial(number))


if __name__ == "__main__":
    main()
