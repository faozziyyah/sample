print("select an operation to perform: ")

print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
print("5. MODULUS")

operation = input()

if operation == "1":
    # code for add
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print("The sum is " + str(int(num_1) + int(num_2))) 
elif operation == "2":
    # code for subtract
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print("The difference is " + str(int(num_1) - int(num_2)))
elif operation == "3":
    # code for multiply
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print("The product is " + str(int(num_1) * int(num_2))) 
elif operation == "4":
    # code for divide
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print("The answer is " + str(int(num_1) / int(num_2))) 
elif operation == "5":
    # code for divide
    num_1 = input("Enter first number: ")
    num_2 = input("Enter second number: ")
    print("The modulus is " + str(int(num_1) // int(num_2))) 
else:
    print("invalid entry")
    
