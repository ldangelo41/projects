def encrypt(plaintext):

    result = [] # empty list to store encrypted values

    for letter in plaintext: # going through letter by letter in sentence

        l = ord(letter) - 79 # encryption key

        result.append(l)

    print("This is your encrypted message")

    for numbers in result:

        print(numbers, end='' )
        print("  ", end='')

    print()
    decrypt(result)



def decrypt(result):


    end_string = "" # empty string

    for numbers in result:
        l = int(numbers)
        l = l + 79
        l = chr(l)
        end_string = end_string + l

    print("Your decrypted message is: ")
    print(end_string)



def main():

    s = input("Input a sentence that you want encrypted: ")

    encrypt(s)

main()