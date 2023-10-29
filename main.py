password = ''
encoded_pass = ''

def menu():
    print("-------------\n1. Encode\n2. Decode\n3. Quit")

menu()

while True:
    option = input("Please enter an option: ")

    if option == '1':
        password = input("Please enter a password to encode: ")
        if password.isdigit():
            encoded_pass = str(int(password) * 2)
            print("Your password has been encoded and stored!")
        else:
            print("Please enter a valid password")
    elif option == '2':
        if encoded_pass:
            print(f'The encoded password is {encoded_pass} and the original password is {password}.')
        else:
            print("No password has been encoded yet!")
    elif option == '3':
        break
    else:
        print("Please select a valid number 1-3")
