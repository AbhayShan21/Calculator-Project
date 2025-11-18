# import art
#
# def add(n1, n2):
#     return n1 + n2
#
# # TODO: Write out the other 3 functions - subtract, multiply and divide.
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2
#
#
# # TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"
#
# operations = {
#     "+" : add, "-" : subtract, "*" : multiply, "/" : divide
# }
#
#
# # TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
#
# # print(operations["*"](4 , 8))
# def calculator():
#     print(art.logo)
#     should_accumulate = True
#     num1 = float(input("What is the first number?: "))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("Chose a mathematical operator: ")
#         num2 = float(input("What is the next number?: "))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 33)
#             calculator()
#
# calculator()

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(art.logo)

    # get first number (validate)
    while True:
        try:
            num1 = float(input("What is the first number?: "))
            break
        except ValueError:
            print("Invalid number input ❌ — please enter a valid number.")

    while True:
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Choose a mathematical operator: ")
        if operation_symbol not in operations:
            print("Invalid operator ❌ — choose one of: + - * /")
            continue

        # get next number (validate, and prevent division by zero)
        while True:
            try:
                num2 = float(input("What is the next number?: "))
            except ValueError:
                print("Invalid number input ❌ — please enter a valid number.")
                continue

            if operation_symbol == "/" and num2 == 0:
                print("Cannot divide by zero ❌ — enter a different number.")
                continue

            break  # num2 is valid

        # perform operation (safe now)
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # ask whether to continue with answer or start new calculation
        while True:
            choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
            if choice == "y":
                num1 = answer
                break  # continue main loop with updated num1
            elif choice == "n":
                # restart: clear screen visually and ask for new first number
                print("\n" * 33)
                calculator()
                while True:
                    try:
                        num1 = float(input("What is the first number?: "))
                        break
                    except ValueError:
                        print("Invalid number input ❌ — please enter a valid number.")
                break  # continue main loop with new num1
            else:
                print("Invalid input ❌ — please type 'y' or 'n'.")

calculator()




