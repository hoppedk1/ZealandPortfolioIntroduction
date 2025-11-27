# Threshold in percent
$Threshold = 10

# Get disk usage for the root filesystem (C: on Windows)
# Adjust the drive letter if needed
$drive = "C:"

# Get free percentage
$disk = Get-PSDrive -Name $drive
$freePercent = [math]::Round(($disk.Free / $disk.Used + $disk.Free) * 100, 2)

# Alternatively, calculate used percent directly
$usedPercent = 100 - $freePercent

if ($usedPercent -ge (100 - $Threshold)) {
    Write-Host "Warning: Less than $Threshold% disk space remaining!"
} else {
    Write-Host "Disk space is fine. $freePercent% free remaining."
}
