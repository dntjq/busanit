def add(a, b):
    return a + b

print(add(5,3))


def add_mul(choice, *args): 
     if choice == "add": 
         result = 0 
         for i in args: 
             result = result + i 
     elif choice == "mul": 
         result = 1 
         for i in args: 
             result = result * i 
     return result 
 
 
  result = add_many(1,2,3)
    print(result)

    result = add_many(1,2,3,4,5,6,7,8,9,10)
    print(result)