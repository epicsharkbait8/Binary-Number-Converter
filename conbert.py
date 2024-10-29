def decimalToBinary(num):
    binary_string = bin(num)[2:]
    print(binary_string)
theThing = int(input("what ya want"))
if theThing >= 0:
    decimalToBinary(theThing)
else:
    print("you put something that doesn't work, stop dat >:(")