def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    
    Args:
        text (str): The input text to encrypt or decrypt
        shift (int): The number of positions to shift each letter
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted or decrypted text
    """
    if mode == 'decrypt':
        shift = -shift
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Convert to number (a=0, b=1, ..., z=25)
            char_num = ord(char) - ord('a')
            
            # Apply the shift with wrapping
            shifted_num = (char_num + shift) % 26
            
            # Convert back to character
            shifted_char = chr(shifted_num + ord('a'))
            
            # Restore original case
            if is_upper:
                shifted_char = shifted_char.upper()
            
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def get_user_input():
    """
    Gets user input for the Caesar Cipher operation.
    
    Returns:
        tuple: (text, shift, mode)
    """
    print("=== Caesar Cipher Program ===")
    print()
    
    # Get the text
    text = input("Enter the text to encrypt/decrypt: ")
    
    # Get the shift value
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get the mode
    while True:
        mode = input("Choose mode (E for encrypt, D for decrypt): ").lower()
        if mode in ['e', 'encrypt']:
            mode = 'encrypt'
            break
        elif mode in ['d', 'decrypt']:
            mode = 'decrypt'
            break
        else:
            print("Please enter 'E' for encrypt or 'D' for decrypt.")
    
    return text, shift, mode


def display_result(original_text, result_text, shift, mode):
    """
    Displays the result of the Caesar Cipher operation.
    
    Args:
        original_text (str): The original input text
        result_text (str): The encrypted or decrypted text
        shift (int): The shift value used
        mode (str): The mode used ('encrypt' or 'decrypt')
    """
    print("\n" + "="*50)
    print(f"Operation: {mode.capitalize()}")
    print(f"Shift value: {shift}")
    print(f"Original text: {original_text}")
    print(f"Result: {result_text}")
    print("="*50)


def main():
    """
    Main function to run the Caesar Cipher program.
    """
    while True:
        try:
            # Get user input
            text, shift, mode = get_user_input()
            
            # Perform the encryption or decryption
            result = caesar_cipher(text, shift, mode)
            
            # Display the result
            display_result(text, result, shift, mode)
            
            # Ask if user wants to continue
            print()
            continue_choice = input("Do you want to perform another operation? (y/n): ").lower()
            if continue_choice not in ['y', 'yes']:
                print("Thank you for using the Caesar Cipher program!")
                break
            print()
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()