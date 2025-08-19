# Password Complexity Checker

A simple Python tool that assesses password strength and provides security recommendations.

## Features

- Secure password input (hidden while typing)
- Strength assessment based on 5 criteria
- Specific improvement recommendations
- Password security tips
- Interactive command-line interface

## Requirements

- Python 3.x

## Usage

```bash
python password_checker.py
```

Select from menu options:
- Check password strength
- View password tips
- Exit

## Password Criteria

The tool evaluates passwords based on:
- Length (minimum 8 characters)
- Uppercase letters (A-Z)
- Lowercase letters (a-z) 
- Numbers (0-9)
- Special characters (!@#$%^&*)

## Strength Levels

- **Very Strong** - All 5 criteria met
- **Strong** - 4 criteria met
- **Moderate** - 3 criteria met
- **Weak** - 2 criteria met
- **Very Weak** - 1 or fewer criteria met

## Example

```
Enter your password: [hidden input]
Entered Password: P#######d
Password Strength: Strong (4 out of 5 criteria met)
Password Length: 9 characters

Recommendations:
• Add special characters (!@#$%^&*)
```
