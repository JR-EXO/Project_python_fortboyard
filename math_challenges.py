import random



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def math_challenge_factorial():
    n = random.randint(1, 10)
    answer = input("What is the factorial of %d? " % n)
    if int(answer) == factorial(n):
        print("You have won a key!")
        return True
    else:
        return False


def solve_linear_equation():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b / float(a)
    return a,b,x


def math_challenge_equation():
    a, b, x = solve_linear_equation()
    answer = input("What is the value of x for the equation %dx + %d = 0? " % (a, b))
    if float(answer) == x:
        print("You have won a key!")
        return True
    else:
        return False


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def nearest_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n


def math_challenge_prime():
    n = random.randint(1, 10)
    answer = input("What is the nearest prime number to %d? " % n)
    if int(answer) == nearest_prime(n):
        print("You have won a key!")
        return True
    else:
        return False


def math_roulette_challenge():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    c = random.randint(1, 20)
    d = random.randint(1, 20)
    e = random.randint(1, 20)

    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        result = a + b + c + d + e
        question = f"What is the sum of {a}, {b}, {c}, {d}, and {e}? "
    elif operation == '-':
        result = a - b - c - d - e
        question = f"What is the result of {a} - {b} - {c} - {d} - {e}? "
    else:  # operation == '*'
        result = a * b * c * d * e
        question = f"What is the product of {a}, {b}, {c}, {d}, and {e}? "

    answer = input(question)

    if int(answer) == result:
        print("You have won a key!")
        return True
    else:
        return False


def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_equation, math_challenge_prime, math_roulette_challenge]
    challenge = random.choice(challenges)
    return challenge()
