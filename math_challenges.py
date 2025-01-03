import random

##Factorial Challenge
def factorial(n):
    if n == 0:
        return 1
    else :
        r=1
        for i in range(1,n+1):
            r = r * i
        return r

def math_challenge_factorial():

    n = random.randint(1,10)
    res = factorial(n)
    print("Math challenge: Calculate the factorial of", n)
    answer = int(input("Your answer: "))

    if res == answer:
        print("Correct! You win a key.")
        return True
    else :
        print("This answer isn't correct.")
        return False


##Equation challenge
def solve_linear_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = -b/a
    return a, b, x

def math_challenge_equation():

    values = solve_linear_equation()
    res = values[2]
    print(f"Math challenge: Solve the equation {values[0]}x + {values[1]} = 0")
    answer = float(input("What is the value of x? : "))

    if res == answer:
        print("Correct! You win a key.")
        return True
    else :
        print("This answer isn't correct.")
        return False


##Prime numbers challenge
def is_prime(n):
    if n < 2:
        return False

    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nearest_prime(n):
    while not is_prime(n):
        n += 1
    return n

def math_challenge_prime():
    n = random.randint(10,20)
    res = nearest_prime(n)
    print(f"Find the nearest prime number to {n}.")
    answer = int(input("Your answer: "))
    if res == answer:
        print("Correct! You win a key.")
        return True
    else :
        print("This answer isn't correct.")
        return False


##Math roulette challenge
def math_roulette_challenge():

    random_numbers = [random.randint(1,20) for _ in range(5)]
    print(f"Numbers on the roulette: {random_numbers}")

    operator = random.choice(["addition", "subtraction", "multiplication"])
    print(f"Calculate the result by combining these numbers with {operator}.")

    if operator == "addition":
        res = 0
        for i in random_numbers:
            res += i
            print(res)
    elif operator == "subtraction":
        res = random_numbers[0]
        for i in range (1,len(random_numbers)):
            res -= i
    elif operator == "multiplication":
        res = 1
        for i in random_numbers:
            res *= i

    answer = int(input("Your answer: "))
    if res == answer:
        print("Correct! You win a key.")
        return True
    else :
        print("This answer isn't correct.")
        return False


def math_challenge():
    challenges = [math_challenge_factorial, math_challenge_equation, math_challenge_prime]
    challenge = random.choice(challenges)
    return challenge()