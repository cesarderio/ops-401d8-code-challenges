import time

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

def main():
    while True:
        print("1: Offensive")
        print("2: Defensive")
        print("0: Exit")
        mode = int(input("Select task (0 to exit): "))
        
        if mode == 1:
            file_path = input("Enter (wordlist) file path: ")
            Off(file_path)
        elif mode == 2:
            file_path = input("Enter (wordlist) file path: ")
            target_word = input("Enter target word: ")
            Def(file_path, target_word)
        elif mode == 0:
            break
        else:
            print("Invalid, please select available mode")

if __name__ == "__main__":
    main()
