
def decimal_to_binary(number):
    binary_string = bin(number)[2:]
    print(binary_string)
user_input = int(input("what ya want"))
if user_input >= 0:
    decimal_to_binary(user_input)
else:
    print("you put something that doesn't work, stop dat >:(")


def binary_to_decimal(binary_str):
    decimal_number = int(binary_str, 2)
    print(decimal_number)

user_input2 = int(input("what ya want"))
if all(char in '01' for char in user_input):
    binary_to_decimal(user_input)
else:
    print("you put something that doesn't work, stop dat >:(")
