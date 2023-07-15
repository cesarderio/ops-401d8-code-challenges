# Define the password policy requirements
$minLength = 6
$minConsecutiveChars = 2

# Get the current password policy settings
$policy = Get-WmiObject -Class Win32_AccountPolicy -Namespace "root\RSOP\Computer" | Select-Object -ExpandProperty PasswordPolicy

# Update the password policy settings
$policy.PasswordHistorySize = 0
$policy.MinimumPasswordLength = $minLength
$policy.MaximumPasswordAge = -1
$policy.PasswordComplexity = $true
$policy.RequireLogonToChangePassword = $true
$policy.RequireUniquePassword = $true

# Set the password policy requirements for the user's account name and full name
$policy.EnableReversibleEncryption = $false
$policy.ClearTextPassword = $false
$policy.MinimumPasswordAge = 0
$policy.PasswordProperties = ($minLength, $minConsecutiveChars)

# Save the updated password policy settings
$policy.Put()
