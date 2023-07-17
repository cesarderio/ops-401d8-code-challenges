# Ops Challenge - File Encryption Script Part 1 of 3

## Overview

Encryption of data at rest is a common need in security operations. Today you will begin development of a Python script that encrypts a single file.

## Resources

[PyPi: cryptography 3.1.1](https://pypi.org/project/cryptography/)
[How to Encrypt and Decrypt Files in Python](https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python)

## Requirements

In Python, create a script that utilizes the cryptography library to:

* Prompt the user to select a mode:
  * Encrypt a file (mode 1)
  * Decrypt a file (mode 2)
  * Encrypt a message (mode 3)
  * Decrypt a message (mode 4)

* If mode 1 or 2 are selected, prompt the user to provide a filepath to a target file.

* If mode 3 or 4 are selected, prompt the user to provide a cleartext string.

Depending on the selection, perform one of the below functions. You’ll need to create four functions:

* Encrypt the target file if in mode 1.
  * Delete the existing target file and replace it entirely with the  encrypted version.
* Decrypt the target file if in mode 2.
  *Delete the encrypted target file and replace it entirely with the decrypted version.
* Encrypt the string if in mode 3.
  * Print the ciphertext to the screen.
* Decrypt the string if in mode 4.
  * Print the cleartext to the screen.

## Stretch Goals (Optional Objectives)

Pursue these stretch goals if you are an advanced user or have remaining lab time.

* Prompt the user if the output file should be compressed to an archive.
* If the user responds ‘y’ for yes, compress the resulting file to an archive.
  * Refer to [How to Compress and Decompress Files in Python](https://www.thepythoncode.com/article/compress-decompress-files-tarfile-python) or use the ***os*** library to perform OS-specific archival commands.

## Background Notes

The fernet module of the cryptography package has built in functions for:

* Generation of the key
* Encryption of plaintext into ciphertext
* Decryption of ciphertext into plaintext

The module guarantees that data encrypted using it cannot be further manipulated or read without the key.

**Methods used**

* `generate_key()`
  * This method generates a new fernet key.
  * This key needs to be kept safe, if the key is lost then the message can no longer be decrypted.
  * If an intruder or hacker gets access to the key they can not only read the data but also forge the data.
* `encrypt(data)`
  * This method encrypts data passed as a parameter to the method.
  * **Parameters**
    * `data (bytes)`: The plaintext to be encrypted.
    * The encrypt method will throw an error if the data is not in bytes.
  * **Return value**: A ciphertext that cannot be read or altered without the key. It is URL-safe base64-encoded and is referred to as Fernet token.
    * The outcome of this is known as a "Fernet token" which is basically ciphertext.
    * The encrypted token also contains the current timestamp (in plaintext) when it was generated.

* `decrypt(token, ttl=None)`
  * This method decrypts the Fernet token passed as a parameter to the method. When it works, the original plaintext is obtained as a result.
  * **Parameters**
    * `token(bytes)`: The Fernet token (ciphertext) to be used for decryption.
    * `ttl (int)`: Optional - An integer can be provided as second parameter in the decrypt method. The ttl shows the time in seconds which a token will be valid. If the token is older than ttl seconds an error will happen. If the ttl is not passed as a parameter, then age of the token is not considered.
  * **Return value**: Returns the original plaintext

**Examples**

First you need to install the cryptography package: `pip install cryptography`

```python
# Fernet module is imported from the cryptography package
from cryptography.fernet import Fernet

# Key is generated
key = Fernet.generate_key()

# Value of key is assigned to a variable
f = Fernet(key)

# The plaintext is converted to ciphertext
token = f.encrypt(b"welcome to cybersecurity")

# Display the ciphertext
print(token)

# Decrypting the ciphertext
d = f.decrypt(token)

# Display the plaintext
print(d)
```

**Output** - decrypted output has a `b` in front of the original message, indicating the byte format. This can be removed using the decode() method while printing the original message.

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet

# Declare Functions

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

# Main

# Generate and write a new key
write_key()

# load the previously generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

message = "hello friend".encode()
print("Plaintext is " + str(message.decode('utf-8')))

# Initialize the Fernet class
f = Fernet(key)

# Encrypt the message
encrypted = f.encrypt(message)

# Print how it looks
print("Ciphertext is " + encrypted.decode('utf-8'))
```
