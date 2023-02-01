import random

# Take the following functions written in Javascript and re-write them in Python.

# 1. Reverse String
# function reverseString(str){
#     return str.split("").reverse().join("")
# }

# console.log(reverseString("Hello World")) // "dlroW olleH"



def reverse_string(str):
    return str[::-1]

my_string = "Hello Jhony, how does it feel to be 30 years old"

print(reverse_string(my_string))



# 2. Fizz Buzz
# function fizzBuzz(num){
#     for (let index = 0; index < num; num++){
        
#         let result = ""

#         if (index % 3 === 0){
#             result = result + "fizz"
#         }

#         if (index % 5 === 0){
#             result = result + "buzz"
#         }

#         console.log(`${index} = `, result)
#     }
# }

# fizzBuzz(16)


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
# function calculator(num1, num2, operation){
#     if (operations = "+"){
#         return num1 + num2
#     }
#     if (operations = "-"){
#         return num1 - num2
#     }
#     if (operations = "*"){
#         return num1 * num2
#     }
#     if (operations = "/"){
#         return num2 !== 0 ? num1/num2 : "Can't Divide by 0"
#     }
# }

# calculator(2,2,"+") //4



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
# function randomNumber(low, max){
#     while (true){
#         const randomNum = Math.floor(Math.random() * max)

#         if(randomNum >= low && randomNum <= max){
#             return randomNum
#         }
#     }
# }

# console.log(randomNumber(10,20)) //random number between 10 and 20



def random_number(low, max):
    random_num = random.randint(low,max)
    return random_num
    
print(random_number(10, 20))  #random number between 10 and 20




# 5. Map
# const map = (arr, callback) => {

#     const newArray = [];

#     for (let index = 0; index < arr.length; index++){
#         newArray.push(callback(arr[index], index))
#     }
#     return newArray
# }

# console.log(map([1,2,3,4], (item, index) => item + 1)) // [2,3,4,5]

def map(arr, cb):
    
    new_array = []
    for i in range(len(arr)):
        new_array.append(cb(arr[i], i))
        
    return new_array

print(map([1,2,3,4],lambda item, index: item + 1))



#6. filter
# const filter = (arr, callback) => {

#     const newArray = []

#     for(let index = 0; index < arr.length; index++){
#         if (callback(arr[index], index)){
#             newArray.push(arr[index])
#         }
#     }
#     return newArray
# }

# console.log(filter([1,2,3,4,5], (item, index) => item % 2 === 0)) //[2,4]


def filter(arr, cb):
    
    new_array = []
    
    for i in range(len(arr)):
        if(cb(arr[i], i) == True):
            new_array.append(arr[i])
    return new_array

print(filter([1,2,3,4,5,6,7,8,9],lambda item, index: item % 2 == 0))


# 7. makePerson
# const makePerson = (name, age) => {
#     return {
#         name: name,
#         age: age
#     }
# }

# console.log(makePerson("Alex", 35)) //{ name: "Alex", age: "35" }


def make_person(name, age):
    return {"name": name, "age": age}

print(make_person("Alex", 35))


