password = ''
encoded_pass = ''

def menu():
    print("-------------\n1. Encode\n2. Decode\n3. Quit")

def encode(password):
    encoded_password = ''
    for char in password:
        if char.isdigit():
            new_digit = str(int(char) + 3)
            encoded_password += new_digit
        else:
            encoded_password += char
    return encoded_password

def decode(password):
    decoded_password = ''
    for char in password:
        if char.isdigit():
            new_digit = str(int(char) - 3)
            decoded_password += new_digit
        else:
            decoded_password += char
    return decoded_password
menu()

while True:
    option = input("Please enter an option: ")

    if option == '1':
        password = input("Please enter a password to encode: ")
        encoded_pass = encode(password)
        print("Your password has been encoded and stored!")
    elif option == '2':
        if encoded_pass:
            decoded_password = decode(encoded_pass)
            print(f'The encoded password is {encoded_pass} and the original password is {decoded_password}.')
        else:
            print("No password has been encoded yet!")
    elif option == '3':
        break
    else:
        print("Please select a valid number 1-3")
