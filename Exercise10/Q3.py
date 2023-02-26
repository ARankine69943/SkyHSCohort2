import getpass

supplied_pin = getpass.getpass(prompt= "Enter your PIN:")

pin = ("1234")


while supplied_pin != pin:
    print("Incorrect PIN number, 2 attempts remaining")
    supplied_pin = getpass.getpass(prompt= "Enter your PIN:")
    if supplied_pin != pin:
        print("Incorrect PIN number, 1 attempt remaining")
        supplied_pin = getpass.getpass(prompt= "Enter your PIN:")
        if supplied_pin != pin:
            print("Incorrect PIN number, card blocked")
            break

if supplied_pin == pin:
    print("PIN Accepted")
