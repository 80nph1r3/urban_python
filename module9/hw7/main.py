def is_prime(func):
    def wrapper(*args, **kwargs):
        num = func(*args)
        for i in range(2, num + 1):
            if i == num:
                print("Простое")
                return num
            if num % i == 0:
                print("Составное")
                return num

    return wrapper


@is_prime
def sum_three(num1: int, num2: int, num3: int) -> int:
    return num1 + num2 + num3


if __name__ == "__main__":
    print(sum_three(2, 3, 6))
