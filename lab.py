# 1. Reverse String

def reverse_string(str):
    return str[::-1]

my_string = "Hello Jhony, how does it feel to be 30 years old"

print(reverse_string(my_string))

# 2. Fizz Buzz
def fizz_buzz(num):
    i = 0
    while(i < num):
        result = ""
        if(i % 3 == 0 and i % 5 == 0):
            result += "fizzbuzz"
        elif(i % 3 == 0):
            result += "fizz"
        elif(i % 5 == 0):
            result = result + "buzz"
        else:
            result += "' '"   
        i += 1
        print(f"{i} = {result}")

fizz_buzz(16)            

# 3. Calculator
def calculator(num1, num2, operation):
    if(operation == "+"):
        return num1 + num2
    if(operation == "-"):
        return num1 - num2
    if(operation == "*"):
        return num1 * num2
    if(operation == "/"):
        return num1 / num2 if num2 != 0 else "Can't Divide by 0"
    
print(calculator(0,3,"/"))

# 4. randomNumber
# def random_number(low, max):
    