# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/18/2023
# Purpose:                      Create a powershell script that enables Bitlocker and initializes the Full Disk Encryption (FDE) process on the specified drive

# Temporarily bypass the execution policy
Set-ExecutionPolicy Bypass -Scope Process -Force

# Set the drive letter or mount point for encryption
$driveLetter = "C:"

# Enable BitLocker and start encryption
$encryptionStatus = (Get-BitLockerVolume -MountPoint $driveLetter).EncryptionPercentage
if ($encryptionStatus -eq $null) {
    # BitLocker is not enabled on the drive, enable it
    Enable-BitLocker -MountPoint $driveLetter -EncryptionMethod "AESTwofishAES" -UsedSpaceOnly
} else {
    Write-Host "BitLocker is already enabled on the drive."
    exit
}

# Revert the execution policy back to its original state
Set-ExecutionPolicy -Scope Process -Default

# End
