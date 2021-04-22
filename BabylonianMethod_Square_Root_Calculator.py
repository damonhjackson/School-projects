# computes the square root of the value using babylonian method
def babylonian_method(a):
    x0 = a / 2
    check = 1
    accuracy = 0.0001
    while check > accuracy:
        x1 = 0.5 * (x0 + (a / x0))
        check = x0 - x1
        x0 = x1
    return x0


# prompt the user to enter an integer value above zero
# check to ensure that the value is indeed above zero
# if not, program displays error message and ask for input again
# displays the square root to user formatted to 3 decimal places
user_number = float(input("Enter an integer greater than 0:"))
if user_number <= 0:
    print("Invalid Input. Enter an integer greater than 0")
else:
    decimal_format = "{:.3f}".format(babylonian_method(user_number))
    print("The square root of " + str(user_number) + " is " + decimal_format)
