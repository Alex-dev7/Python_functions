# sub_nums that takes two arguments and returns their difference
def sub_nums(x,y):
    return x - y

print(sub_nums(4,2))

# say_hello that takes a name as an arguments and says hello to that name
def say_hello(name):
    print(f"Hello {name}")
    
say_hello("Jhony")

# sayhelloadv that takes a dictionary with a name and age property and prints "hello {name}, how does it feel to be {age} years old"
dic = {"name": "Jhony", "age": 30}

def sayhelloadv(dict):
    print(f"Hello {dict['name']}, how does it feel to be {dict['age']} years old")
    
sayhelloadv(dic)

# looper takes one array as an argument, it loops over the array and prints each item individually

num_list = [1,2,3,4,5,6,7,8,9,10]

def looper(arr):
    for item in arr:
        print(item)

looper(num_list)