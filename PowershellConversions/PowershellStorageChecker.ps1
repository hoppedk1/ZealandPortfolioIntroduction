# Tjekker C driver
$drive = Get-PSDrive -Name C

# Udregning
$remainingSpace = ($drive.Free / $drive.Used) * 100

# Output
Write-Host "Remaining space on C: drive: $($remainingSpace)%"

if ($remainingSpace -lT 10){
Write-Warning "The remaining space is less than 10%"
}
