import random
import time

def generate_problem(num_digits, operation):
    if operation == "add":
        num1 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        num2 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        problem = (num1,'+',num2)
        answer = num1 + num2
        return problem,answer
    elif operation == "subtract":
        num1 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        num2 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        if num2 > num1:
            num1, num2 = num2, num1
        answer = num1 - num2
        problem = (num1,'-',num2)
        return problem,answer
    elif operation == "divide":
        num1 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        num2 = random.randint(2, 10 ** (num_digits - 1))
        answer = num1 / num2
        problem = (num1,'/',num2)
        return problem,answer
    elif operation == "multiply":
        num1 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        num2 = random.randint(10 ** (num_digits - 1), 10 ** num_digits - 1)
        answer = num1 * num2
        problem = (num1 * num2)
        return problem,answer

def arithmetic_practice():
    print("Welcome to the Arithmetic Practice Tool!")
    operation = input("Choose an operation (add, subtract, divide, multiply): ")
    num_digits = int(input("Choose the maximum number of digits (e.g., 2 for 10-99): "))
    time_delay = int(input("Choose the time delay before displaying the answer (in seconds): "))
    num_problems = int(input("How many problems do you want to solve? "))
    
    for _ in range(num_problems):
        problem, answer = generate_problem(num_digits, operation)
        print(*problem)
        time.sleep(time_delay)
        print("The answer is:",answer,'\n')

if __name__ == "__main__":
    arithmetic_practice()
