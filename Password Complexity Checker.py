import re
import getpass

print("---------------- Password Complexity Checking Tool -----------------")

def assess_password_strength(password):
    # Checking criteria
    has_numbers = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Count met criteria
    criteria = [has_numbers, has_uppercase, has_lowercase, meets_length_requirement, has_special_characters]
    met_criteria_count = sum(criteria)
    
    # Detailed feedback
    feedback = []
    if not meets_length_requirement:
        feedback.append("• Use at least 8 characters")
    if not has_uppercase:
        feedback.append("• Add uppercase letters (A-Z)")
    if not has_lowercase:
        feedback.append("• Add lowercase letters (a-z)")
    if not has_numbers:
        feedback.append("• Add numbers (0-9)")
    if not has_special_characters:
        feedback.append("• Add special characters (!@#$%^&*)")
    
    # Strength classification
    if met_criteria_count == 5:
        strength = "Very Strong (All criteria met)"
    elif met_criteria_count == 4:
        strength = "Strong (4 out of 5 criteria met)"
    elif met_criteria_count == 3:
        strength = "Moderate (3 out of 5 criteria met)"
    elif met_criteria_count == 2:
        strength = "Weak (2 out of 5 criteria met)"
    else:
        strength = "Very Weak (1 or fewer criteria met)"
    
    return strength, feedback

def main():
    while True:
        print("\nSelect an option:")
        print("1. Check password strength")
        print("2. View password tips")
        print("3. Exit")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            # Get password input securely
            password_input = getpass.getpass("Enter your password: ")
            
            if len(password_input) == 0:
                print("Password cannot be empty!")
                continue
            
            # Mask password for display
            if len(password_input) >= 2:
                masked_password = password_input[0] + '#' * (len(password_input) - 2) + password_input[-1]
            else:
                masked_password = '#' * len(password_input)
            
            # Assess password strength
            strength, feedback = assess_password_strength(password_input)
            
            # Display results
            print(f"\nEntered Password: {masked_password}")
            print(f"Password Strength: {strength}")
            print(f"Password Length: {len(password_input)} characters")
            
            if feedback:
                print("\nRecommendations:")
                for suggestion in feedback:
                    print(suggestion)
            else:
                print("\nExcellent! Your password meets all security criteria.")
        
        elif choice == '2':
            print("\nPassword Security Tips:")
            tips = [
                "1. Use at least 12 characters for better security",
                "2. Mix uppercase, lowercase, numbers, and symbols",
                "3. Avoid common words and personal information",
                "4. Don't reuse passwords across accounts",
                "5. Consider using a password manager",
                "6. Enable two-factor authentication when possible",
                "7. Update passwords regularly",
                "8. Avoid predictable patterns (123, abc)"
            ]
            for tip in tips:
                print(tip)
        
        elif choice == '3':
            print("Thank you for using Password Complexity Checker!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
