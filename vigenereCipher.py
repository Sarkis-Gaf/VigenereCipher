import sys

# lets create a function here to repeat the key to match the len of text
def extend_key(text, key):
    key = key.lower() # lowercase 
    key_repeated = "".join(key[i % len(key)] for i in range(len(text)))
    return key_repeated

# Now lets create our function that will encrypt the text
def vigenereCipher(plaintext, key):
    key = extend_key(plaintext, key)
    ciphertext = ""
    
    # lets loop through the text and encrypt it
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k) - ord('a')
            newChar = chr(((ord(p.lower())-ord('a') + shift) % 26) + ord('a'))
            ciphertext += newChar.upper() if p.isupper() else newChar
        else:
            ciphertext += p # if its not a letter, we just add it to the ciphertext

    return ciphertext     

# Now lets create our function that will decrypt the text
def vigenereDecipher(ciphertext, key):
    key = extend_key(ciphertext, key)
    plaintext = ""
    
    # lets loop through the text and decrypt it
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k) - ord('a')
            newChar = chr(((ord(c.lower())-ord('a') - shift) % 26) + ord('a'))
            plaintext += newChar.upper() if c.isupper() else newChar
        else:
            plaintext += c
            
    return plaintext

# Now lets setup our main function 
def main():
    # I felt like a menu would be really good to add so the user can choose what they want to do
    print("Vigenere Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    
    # Here we get user input
    choice = input("Enter choice: ")
    
    # loop to keep the program running
    while choice != '3':
        # lets get the text and key from the user
        text = input("Enter text: ")
        key = input("Enter key: ")
        
        # lets check the choice and call the appropriate function
        if choice == '1':
            print("Ciphertext:", vigenereCipher(text, key))
        elif choice == '2':
            print("Plaintext:", vigenereDecipher(text, key))
        else:
            print("Invalid choice")
        
        # lets get the user input again
        choice = input("Enter choice: ")
        
    print("Goodbye!")
if __name__ == "__main__":
    main()

               