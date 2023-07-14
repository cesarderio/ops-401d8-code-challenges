# convert to a string
"SECRET" | ConvertTo-SecureString -AsPlainText -Force | ConvertTo-SecureString



# Encrypt the secret.txt file
# (Get-Item -Path C:\Users\Administrator\Desktop\secret.txt).Encrypt()
# Decrypt the secret.txt file
# (Get-Item -Path C:\Users\Administrator\Desktop\secret.txt).Decrypt()


# powershell command
Encrypt-File -Path "C:\Users\Administrator\Desktop\secret.txt"
# powershell command
Decrypt-File -Path "C:\Users\Administrator\Desktop\secret.txt"


# start a process for laughs
Start-Process "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley"




# To perform encryption in single file you can run this command

cipher /A /E filename

# To Perform encryption on a list of files

cipher /A /E filename1 filename2 filename3


# To encrypt the directory ,run the below command

cipher /E directoryname

# To encrypt all the files in the folder:
# Run the below command to encrypt all the files in a folder.

cipher  /E directoryname\*

# For Example to encrypt all the files in the folder F:\docs, the command line will be like this

cipher /E  F:\docs\*

# Encrypt a folder including all subfolders
# We can add /S Switch to perform encryption recursively on each of the folders

cipher /E /S :directoryname

# Encrypt folder and files:
#Encrypt a folder and all the files and sub folders in that directory :

cipher /A /E /S: directoryname

# Decrypting files and folders:

# The commands for files and folders decryption are similar to the one mentioned in the above case . You just need to replace the /E to /D.
