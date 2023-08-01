import time
import getpass

def Off(file_path, delay=1):
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()  # remove newline characters
            print(word)
            time.sleep(delay)  # delay in seconds

def Def(file_path, target_word):
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()  # remove newline characters
            if word == target_word:
                print(f"'{target_word}' match found in list.")
                return
    print(f"'{target_word}' no match found in list.")

def check_password_complexity(password, min_length, min_capital, min_numbers, min_symbols):
    complexity_result = {
        "length": len(password) >= min_length,
        "capital_letters": sum(1 for char in password if char.isupper()) >= min_capital,
        "numbers": sum(1 for char in password if char.isdigit()) >= min_numbers,
        "symbols": sum(1 for char in password if not char.isalnum()) >= min_symbols
    }
    return complexity_result

def main():
    while True:
        print("1: Offensive")
        print("2: Defensive")
        print("3: Password Complexity Check")
        print("0: Exit")
        mode = int(input("Select task (0 to exit): "))
        
        if mode == 1:
            file_path = input("Enter (wordlist) file path: ")
            Off(file_path)
        elif mode == 2:
            file_path = input("Enter (wordlist) file path: ")
            target_word = getpass.getpass("Enter target word: ")
            Def(file_path, target_word)
        elif mode == 3:
            password = getpass.getpass("Enter a password: ")
            min_length = int(input("Minimum password length: "))
            min_capital = int(input("Minimum number of capital letters: "))
            min_numbers = int(input("Minimum number of numbers: "))
            min_symbols = int(input("Minimum number of symbols: "))

            complexity_result = check_password_complexity(password, min_length, min_capital, min_numbers, min_symbols)
            print("\nPassword Complexity Check Results:")
            for metric, satisfied in complexity_result.items():
                status = "Satisfied" if satisfied else "Not Satisfied"
                print(f"{metric.capitalize()}: {status}")
            if all(complexity_result.values()):
                print("SUCCESS: Password meets all complexity requirements.")
            else:
                print("Password does not meet all complexity requirements.")

        elif mode == 0:
            break
        else:
            print("Invalid, please select an available mode")

if __name__ == "__main__":
    main()
