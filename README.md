# Image Encryption Tool

A Python tool for encrypting and decrypting images using pixel manipulation and mathematical operations.

## Features

- Encrypt images using mathematical operations on pixel values
- Decrypt images back to original form
- Simple command-line interface
- Supports common image formats (JPG, PNG, BMP, etc.)

## Requirements

- Python 3.x
- PIL (Pillow)
- NumPy

## Installation

```bash
pip install Pillow numpy
```

## Usage

```bash
python image_encryption.py
```

Select from the menu:
- `e` - Encrypt an image
- `d` - Decrypt an image  
- `q` - Quit program

## How it Works

The tool applies mathematical operations to each pixel value:
- **Encryption**: Adds the key value to each pixel
- **Decryption**: Subtracts the key value from each pixel
- Uses modular arithmetic to keep values in valid range (0-255)

## Example

```
Enter encryption key: 50
Enter the path to the image: photo.jpg
Image encrypted successfully. Saved at: encrypted_image.png
```

## Files Generated

- `encrypted_image.png` - Output of encryption process
- `decrypted_image.png` - Output of decryption process
