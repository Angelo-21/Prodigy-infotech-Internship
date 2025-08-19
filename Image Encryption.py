from PIL import Image
import numpy as np

print("------------- Image Encryption Tool --------------")

def encrypt_image(image_path, key):
    # Opening the image
    original_image = Image.open(image_path)
    # Converting the image to a NumPy array
    image_array = np.array(original_image)
    # Applying mathematical operation to each pixel using the key
    encrypted_image_array = (image_array + key) % 256
    # Creating a new image from the encrypted NumPy array
    encrypted_image = Image.fromarray(np.uint8(encrypted_image_array))
    # Saving the encrypted image
    encrypted_image_path = "encrypted_image.png"
    encrypted_image.save(encrypted_image_path)
    print(f"Image encrypted successfully. Saved at: {encrypted_image_path}")

def decrypt_image(encrypted_image_path, key):
    # Opening the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    # Converting the image to a NumPy array
    encrypted_image_array = np.array(encrypted_image)
    # Reversing the encryption using the key
    decrypted_image_array = (encrypted_image_array - key) % 256
    # Creating a new image from the decrypted NumPy array
    decrypted_image = Image.fromarray(np.uint8(decrypted_image_array))
    # Saving the decrypted image
    decrypted_image_path = "decrypted_image.png"
    decrypted_image.save(decrypted_image_path)
    print(f"Image decrypted successfully. Saved at: {decrypted_image_path}")

def main():
    while True:
        print("\nSelect an option:")
        print("e - Encrypt image")
        print("d - Decrypt image")
        print("q - Quit")
        choice = input("Your choice: ")
        
        if choice == 'e':
            encrypt_choice()
        elif choice == 'd':
            decrypt_choice()
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def encrypt_choice():
    key = int(input("Enter encryption key: "))
    image_location = input("Enter the path to the image: ")
    try:
        encrypt_image(image_location, key)
    except FileNotFoundError:
        print("Image not found. Please check the path and try again.")

def decrypt_choice():
    key = int(input("Enter decryption key: "))
    encrypted_image_location = input("Enter the path to the encrypted image: ")
    try:
        decrypt_image(encrypted_image_location, key)
    except FileNotFoundError:
        print("Encrypted image not found. Please check the path and try again.")

if __name__ == "__main__":
    main()
