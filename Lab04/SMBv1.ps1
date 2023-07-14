# Define the desired SMB v1 client driver configuration
$desiredConfiguration = 1

# Check if SMB v1 client driver configuration is already set to the desired value
$existingConfiguration = Get-SmbClientConfiguration | Select-Object -ExpandProperty EnableSMB1Protocol
if ($existingConfiguration -eq $desiredConfiguration) {
    Write-Host "SMB v1 client driver configuration is already set to the desired value."
} else {
    # Set the SMB v1 client driver configuration to the desired value
    Set-SmbClientConfiguration -EnableSMB1Protocol $desiredConfiguration

    # Verify if the configuration change was successful
    $newConfiguration = Get-SmbClientConfiguration | Select-Object -ExpandProperty EnableSMB1Protocol
    if ($newConfiguration -eq $desiredConfiguration) {
        Write-Host "SMB v1 client driver configuration has been set to the desired value."
    } else {
        Write-Host "Failed to set SMB v1 client driver configuration to the desired value."
    }
}
