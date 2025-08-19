# Caesar Cipher Program for Beginners

def encrypt_text(message, shift):
    """Encrypts a message using Caesar Cipher"""
    encrypted = ""
    
    for letter in message:
        if letter.isalpha():  # Check if it's a letter
            # Convert to uppercase for simplicity
            letter = letter.upper()
            
            # Get the position of letter (A=0, B=1, etc.)
            position = ord(letter) - ord('A')
            
            # Shift the position
            new_position = (position + shift) % 26
            
            # Convert back to letter
            new_letter = chr(new_position + ord('A'))
            encrypted = encrypted + new_letter
        else:
            # Keep spaces and punctuation as they are
            encrypted = encrypted + letter
    
    return encrypted


def decrypt_text(message, shift):
    """Decrypts a message using Caesar Cipher"""
    decrypted = ""
    
    for letter in message:
        if letter.isalpha():  # Check if it's a letter
            # Convert to uppercase for simplicity
            letter = letter.upper()
            
            # Get the position of letter (A=0, B=1, etc.)
            position = ord(letter) - ord('A')
            
            # Shift backwards
            new_position = (position - shift) % 26
            
            # Convert back to letter
            new_letter = chr(new_position + ord('A'))
            decrypted = decrypted + new_letter
        else:
            # Keep spaces and punctuation as they are
            decrypted = decrypted + letter
    
    return decrypted


# Main program
print("Caesar Cipher Encryption/Decryption Tool")
print("=" * 40)
print("This program can encrypt and decrypt messages using Caesar Cipher.")
print()

while True:
    # Get user's choice
    print("Select an option:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit program")
    print("-" * 30)
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == '1':
        # Encrypt
        print("\nENCRYPTION MODE")
        print("-" * 20)
        message = input("Enter message to encrypt: ")
        
        # Get shift with validation
        while True:
            try:
                shift = int(input("Enter shift value (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Error: Please enter a number between 1 and 25.")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        result = encrypt_text(message, shift)
        print(f"\nOriginal message: {message}")
        print(f"Encrypted message: {result}")
        print(f"Shift value used: {shift}")
        
        # Ask if they want to verify by decrypting
        verify = input("\nVerify by decrypting? (y/n): ").lower()
        if verify == 'y' or verify == 'yes':
            decrypted = decrypt_text(result, shift)
            print(f"Verification - Decrypted: {decrypted}")
        
    elif choice == '2':
        # Decrypt
        print("\nDECRYPTION MODE")
        print("-" * 20)
        message = input("Enter encrypted message: ")
        
        # Get shift with validation
        while True:
            try:
                shift = int(input("Enter shift value used for encryption: "))
                if 1 <= shift <= 25:
                    break
                else:
                    print("Error: Please enter a number between 1 and 25.")
            except ValueError:
                print("Error: Please enter a valid number.")
        
        result = decrypt_text(message, shift)
        print(f"\nEncrypted message: {message}")
        print(f"Decrypted message: {result}")
        print(f"Shift value used: {shift}")
        
    elif choice == '3':
        # Exit
        print("\nThank you for using Caesar Cipher Tool.")
        print("Program terminated.")
        break
        
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    print("\n" + "=" * 50)
