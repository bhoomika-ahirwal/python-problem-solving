def is_even(number):
    return number % 2 == 0


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


def factorial(number):
    if number < 0:
        return None

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


def analyze_number(number):
    print("\nNumber Analysis")
    print("----------------")
    print("Number:", number)
    print("Even:", is_even(number))
    print("Prime:", is_prime(number))
    print("Factorial:", factorial(number))


number = int(input("Enter a number: "))
analyze_number(number)  