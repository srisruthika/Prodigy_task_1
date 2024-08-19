def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper()else 97
            shifted_char = chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
            result += shifted_char
        else:
            result += char

    return result

def main():
    print("Welcome to the Caesar Cipher Encryption/Decryption Program! ")
    while True:
        mode = input("Do you want to encrypt or decrypt? ").strip().lower()
        if mode not in ["encrypt", "decrypt"]:
            if mode == 'exit':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid option. Please type 'encrypt', 'decrypt', or 'exit'.")
                continue
        
        message = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value: ").strip())
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")
            continue

        if mode == 'encrypt':
            encrypted_message = caesar_cipher(message, shift, mode)
            print(f"Encrypted message: {encrypted_message}")
        elif mode == 'decrypt':
            decrypted_message = caesar_cipher(message, shift, mode)
            print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
