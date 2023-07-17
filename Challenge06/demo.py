#!/usr/bin/env python3

# Import libraries
from cryptography.fernet import Fernet

# Declare variables

# Declare functions

# Function that handles key generation
def write_key():
    
    # Generate key and save it into a file
    key = Fernet.generate_key()

    # Saving key into a file
    with open("key.key", "wb") as key_file:
        key_file.write(key)

    # Return key
# Function to load the generated key so we can use it to encrypt the data
def load_key():
    return open("key.key", "rb").read()

# Main 

# Generate and write the new key
write_key()

# Load the generated key
key = load_key()
print("Key is " + str(key.decode("utf-8")))

# Encrypt a message

# Message to be encrypted
message = "TOP SECRET!"

print("Plainttext message is " + str(message.decode("utf-8")))

# Do the encryption - Initilize the Fernet module and name it
f = Fernet(key)

# Encrypt the message
encrypted_message = f.encrypt(message)

# Print the encrypted message
print("Encrypted message is " + encrypted_message.decode("utf-8"))
