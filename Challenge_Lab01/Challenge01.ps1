#!/bin/bash

# Script Name:                  
# Author:                       Raphael Chookagian
# Date of latest revision:      07/11/2023
# Purpose:                      Create a script that:
# automates ONE of the following required SOC 2 configurations on a Windows 10 endpoint.
#   * Automatic screen lock
#   * Antivirus installed and scanning
#   * Automatic OS updates enabled


# Declare Variables

# Declare Functions

# Create

# Main


# Enable automatic screen lock
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "ScreenSaveTimeOut" -Value 300
Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name "ScreenSaverIsSecure" -Value 1
Set-ItemProperty -Path "HKCU:\Software\Policies\Microsoft\Windows\Control Panel\Desktop" -Name "ScreenSaverGracePeriod" -Value 0

# Install antivirus software (replace "AntivirusSetup.exe" with the actual installer)
$antivirusInstaller = "C:\Path\To\AntivirusSetup.exe"
Start-Process -Wait -FilePath $antivirusInstaller

# Run antivirus scan (replace "C:\Scan" with folder or drive path)
$scanPath = "C:\Scan"
$antivirusExecutable = "C:\Program Files\Antivirus\antivirus.exe"
Start-Process -Wait -FilePath $antivirusExecutable -ArgumentList "-Scan", "-Path", $scanPath

# Enable automatic OS updates
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WindowsUpdate\Auto Update" -Name "AUOptions" -Value 4
Set-Service -Name "wuauserv" -StartupType Automatic
Start-Service -Name "wuauserv"

# Configure password manager application (replace "PasswordManager.exe" password manager)
$passwordManager = "C:\Path\To\PasswordManager.exe"
Start-Process -Wait -FilePath $passwordManager


# End
