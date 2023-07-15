# Script Name:                  encryption and decryption
# Author:                       Raphael Chookagian
# Date of latest revision:      07/14/2023
# Purpose:                      Create a script that:
# powershell scripts for encrypting and decrypting


# Declare Variables


# Declare Functions

# Create

# Main

# End








# create a new file with hello world inside the file
echo "Hello world!" > secret.txt

# Encrypt the secret.txt file
(Get-Item -Path "C:\Users\Administrator\Desktop\secret.txt").Encrypt()
# Decrypt the secret.txt file
(Get-Item -Path "C:\Users\Administrator\Desktop\secret.txt").Decrypt()

# create a new file with hello world inside
echo "Hello world!" > crypt.txt

# Use openssl to hash using MD5 algorithm and output the hash to crypt.txt file
openssl dgst -md5 -hex -out hashMd5.txt crypt.txt


# base64 encode
echo -n "Never gonna give you up" | openssl enc -base64

# base64 decode
 echo "RmluaXNoZWQgdGhpcyBsYWIhCg==" | openssl enc -d -base64


# encrypt with openssl and aes-256 encryption algorithm
openssl enc -aes-256-cbc -in crypt.txt -out md5crypt.txt -k "solarwinds123" -pbkdf2

# start a process for laughs
Start-Process "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"

# create a new file and add the url inside the file
echo 'Start-Process "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"' > rick.ps1


openssl dgst -md5 rick.ps1
# MD5(rick.sh)= 8cc92ee833a74ea1c65479005a3a2eb8
openssl enc -aes-256-cbc -in rick.ps1 -out encrypted_rick.enc
