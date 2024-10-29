def decimal_to_binary(number):
    binary_string = bin(number)[2:]
    print(binary_string)
user_input = int(input("what ya want"))
if user_input >= 0:
    decimal_to_binary(user_input)
else:
    print("you put something that doesn't work, stop dat >:(")