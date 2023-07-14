# Function to encrypt a file
function Encrypt-File {
  param(
      [Parameter(Mandatory=$true)]
      [string]$FilePath,
      [Parameter(Mandatory=$true)]
      [string]$OutputPath,
      [Parameter(Mandatory=$true)]
      [string]$Password
  )

  $key = (Get-Hash $Password).Substring(0, 32)
  $iv = (Get-Hash ($Password + "IV")).Substring(0, 16)

  $encryptionKey = [System.Convert]::FromBase64String($key)
  $initializationVector = [System.Convert]::FromBase64String($iv)

  $aes = New-Object System.Security.Cryptography.AesManaged
  $aes.Key = $encryptionKey
  $aes.IV = $initializationVector
  $aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
  $aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

  $encryptor = $aes.CreateEncryptor()

  $inputStream = New-Object System.IO.FileStream($FilePath, [System.IO.FileMode]::Open)
  $outputStream = New-Object System.IO.FileStream($OutputPath, [System.IO.FileMode]::Create)

  $cryptStream = New-Object System.Security.Cryptography.CryptoStream($outputStream, $encryptor, [System.Security.Cryptography.CryptoStreamMode]::Write)

  $buffer = New-Object byte[](1024)
  $count = $inputStream.Read($buffer, 0, $buffer.Length)

  while ($count -gt 0) {
      $cryptStream.Write($buffer, 0, $count)
      $count = $inputStream.Read($buffer, 0, $buffer.Length)
  }

  $cryptStream.Close()
  $outputStream.Close()
  $inputStream.Close()
}

# Function to decrypt a file
function Decrypt-File {
  param(
      [Parameter(Mandatory=$true)]
      [string]$FilePath,
      [Parameter(Mandatory=$true)]
      [string]$OutputPath,
      [Parameter(Mandatory=$true)]
      [string]$Password
  )

  $key = (Get-Hash $Password).Substring(0, 32)
  $iv = (Get-Hash ($Password + "IV")).Substring(0, 16)

  $decryptionKey = [System.Convert]::FromBase64String($key)
  $initializationVector = [System.Convert]::FromBase64String($iv)

  $aes = New-Object System.Security.Cryptography.AesManaged
  $aes.Key = $decryptionKey
  $aes.IV = $initializationVector
  $aes.Mode = [System.Security.Cryptography.CipherMode]::CBC
  $aes.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7

  $decryptor = $aes.CreateDecryptor()

  $inputStream = New-Object System.IO.FileStream($FilePath, [System.IO.FileMode]::Open)
  $outputStream = New-Object System.IO.FileStream($OutputPath, [System.IO.FileMode]::Create)

  $cryptStream = New-Object System.Security.Cryptography.CryptoStream($inputStream, $decryptor, [System.Security.Cryptography.CryptoStreamMode]::Read)

  $buffer = New-Object byte[](1024)
  $count = $cryptStream.Read($buffer, 0, $buffer.Length)

  while ($count -gt 0) {
      $outputStream.Write($buffer, 0, $count)
      $count = $cryptStream.Read($buffer, 0, $buffer.Length)
  }

  $outputStream.Close()
  $cryptStream.Close()
  $inputStream.Close()
}

# Function to compute SHA256 hash of a string
function Get-Hash {
  param(
      [Parameter(Mandatory=$true)]
      [string]$InputString
  )

  $sha256 = [System.Security.Cryptography.SHA256]::Create()
  $hashBytes = $sha256.ComputeHash([System.Text.Encoding]::UTF8.GetBytes($InputString))
  $hashString = [System.Convert]::ToBase64String($hashBytes)
  return $hashString
}

# Main script
$ExitRequested = $false

while (-not $ExitRequested) {
  Clear-Host

  Write-Host "----- Main Menu -----"
  Write-Host "1. Hash a file"
  Write-Host "2. Encrypt a file"
  Write-Host "3. Decrypt a file"
  Write-Host "4. Exit"

  $choice = Read-Host "Enter your choice:"

  switch ($choice) {
      1 {
          $FilePath = Read-Host "Enter the path of the file to hash:"
          $hash = Get-Hash -InputString $FilePath
          Write-Host "Hash value: $hash"
          Pause
      }
      2 {
          $FilePath = Read-Host "Enter the path of the file to encrypt:"
          $OutputPath = Read-Host "Enter the output path for the encrypted file:"
          $Password = Read-Host "Enter the encryption password:"
          Encrypt-File -FilePath $FilePath -OutputPath $OutputPath -Password $Password
          Write-Host "File encrypted successfully."
          Pause
      }
      3 {
          $FilePath = Read-Host "Enter the path of the file to decrypt:"
          $OutputPath = Read-Host "Enter the output path for the decrypted file:"
          $Password = Read-Host "Enter the decryption password:"
          Decrypt-File -FilePath $FilePath -OutputPath $OutputPath -Password $Password
          Write-Host "File decrypted successfully."
          Pause
      }
      4 {
          $ExitRequested = $true
      }
      default {
          Write-Host "Invalid choice. Please try again."
          Pause
      }
  }
}
