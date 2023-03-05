pin = ("1234")

supplied_pin = input("Enter your PIN:")

while supplied_pin != pin:
    print("Incorrect PIN number, 2 attempts remaining")
supplied_pin = input("Enter your PIN:")
if supplied_pin != pin:
    print("Incorrect PIN number, 1 attempt remaining")
    supplied_pin = input("Enter your PIN:")
    if supplied_pin != pin:
        print("Incorrect PIN number, card blocked")
#break

if supplied_pin == pin:
    print("PIN Accepted")
