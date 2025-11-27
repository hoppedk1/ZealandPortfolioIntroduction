# Drive letter
$Drive = "C"

# Threshold in percent
$Threshold = 10

# Get disk info
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$Drive'"

# Calculate free percentage
$freePercent = [math]::Round(($disk.FreeSpace / $disk.Size) * 100, 2)

if ($freePercent -le $Threshold) {
    Write-Host "Warning: Less than $Threshold% disk space remaining!"
} else {
    Write-Host "Disk space is fine. $freePercent% free remaining."
}
