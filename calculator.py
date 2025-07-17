import art

def add(n1, n2):
    return n1 + n2

def subtraction(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2


operation = {
    "+" : add,
    "-" : subtraction,
    "*" : multiply,
    "/" : divide,
}


def calculator():
    print(art.logo)
    start_calc = True
    # need this out side so It doesnt reset everytime the while loops
    first_number = float(input("What the first number? "))

    while start_calc == True:
        calc = input("please choose an operation (+ , - , / , *)")
        second_number = float(input("what the second number? "))

        """Calling function with dictionary"""
        #call dictionary first then it will return the name of the function , then we pass in the values and run the function

        answer = operation[calc](first_number,second_number)
        print(f"{first_number} {calc} {second_number} = {answer}")

        run = input(f"Type 'Y' to continue calculating with {answer}, or 'N' to start over: ").upper()
        if run == "Y":
            first_number = answer
        else:
            start_calc = False
            print("Calculation ended.")


calculator()
