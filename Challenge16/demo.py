




import time
import getpass

def iterator():
    filepath = input("Enter file path: ")

    file = open(filepath, 'r')

    line = file.readline()

    # loop
    while line:
        line = line.rstrip()
        word = line
        print (word)
        time.sleep(1)
        line = file.readline()
    file.close()
    

iterator()
