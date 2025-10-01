import logging
import math

logging.basicConfig(
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H-%M",
    level=logging.DEBUG
)

class Negative_number(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes(a, b):
    if a > b:
        a, b = b, a
        logging.info("Input values swapped a=%d b=%d", a, b)
    return [i for i in range(a+1, b) if isprime(i)]

def fib(b):
    if b <= 0:
        raise Negative_number("Length b is negative")
    if b == 1:
        return [0]
    fibb = [0, 1]
    for i in range(2, b):
        fibb.append(fibb[i-1] + fibb[i-2])
    return fibb

def sum_od_digits(n):
    return sum(int(d) for d in str(abs(n)))

def factorial(n):
    if n < 0:
        raise Negative_number("a or b is negative")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def even_odd(a, b):
    if a > b:
        a, b = b, a
        logging.info("Input values swapped a=%d b=%d", a, b)
    even = odd = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return even, odd

try:
    a = int(input("Enter first no: "))
    b = int(input("Enter second no: "))

    print(f"Prime numbers between {a} and {b} are : ", primes(a, b))
    print(f"Fibonacci series upto length {b} is :", fib(b))
    print(f"Sum of digits of {a} is: ", sum_od_digits(a))
    print(f"Sum of digits of {b} is: ", sum_od_digits(b))
    print("Factorial of a is: ", factorial(a))
    print("Factorial of b is: ", factorial(b))
    print("Sum of even and odd b/w a and b is: ", even_odd(a, b))

except ValueError:
    logging.error("Only accepts integer value", exc_info=True)
except Negative_number as ne:
    logging.error("Negative number - %s", ne)
