def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo 26
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters are added unchanged

    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1' or choice.lower() == 'encrypt':
            text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(text, shift, mode='encrypt')
            print(f"Encrypted message: {encrypted_text}\n")

        elif choice == '2' or choice.lower() == 'decrypt':
            text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(text, shift, mode='decrypt')
            print(f"Decrypted message: {decrypted_text}\n")

        elif choice == '3' or choice.lower() == 'exit':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
