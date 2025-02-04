import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters for better security.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    
    password = generate_password(length)
    
    
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
