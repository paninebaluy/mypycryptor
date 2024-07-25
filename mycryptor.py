# import a module that will copy the output to the clipboard, works on Mac
import subprocess


# Encrypt user input
def encrypt(text, number):
    encrypted = ""
    i = 0
    for char in text:
        n = ord(char) + number
        i += 1
        if i % 2 == 0:
            encrypted += chr(n) + "{"
        else:
            encrypted += chr(n) + "|"

    return encrypted


# Decrypt user input
def decrypt(text, number):
    word = ""
    decrypted = ""
    arr = text.split("{")
    # handle cases with zero-length list items
    for part in arr:
        if part != "":
            arr2 = part.split("|")
            fragment = "".join(arr2)
            word += fragment
    # decrypt the word without "{" and "|"
    for char in word:
        n = ord(char) - number
        decrypted += chr(n)

    return decrypted


# Get user input
def get_user_input_enc():
    input_text = input("Enter the text to encrypt: ")
    input_num = input("Enter any number from 1 to 3: ")

    class Input:
        text = input_text
        number = int(input_num)

    if Input.number in range(1, 4):
        return Input
    else:
        print("Wrong number, the script uses 3 by default.")
        Input.number = 3
        return Input


def get_user_input_dec():
    input_text = input("Enter the text to decrypt: ")
    input_num = input("Enter the number you used when encrypting, from 1 to 3: ")

    class Input:
        text = input_text
        number = int(input_num)

    if Input.number in range(1, 4):
        return Input
    else:
        print("Wrong number, try again.")
        return None


def print_encrypted():
    initial = get_user_input_enc()
    encrypted_word = encrypt(initial.text, initial.number)
    # copy the initial word to the buffer
    subprocess.run("pbcopy", text=True, input=encrypted_word)
    print("Input text: " + initial.text)
    print("Encrypted text (copied to your buffer): " + encrypted_word)


def print_decrypted():
    encrypted = get_user_input_dec()
    decrypted_word = decrypt(encrypted.text, encrypted.number)
    print("Decrypted text: " + decrypted_word)


print_encrypted()
print_decrypted()
