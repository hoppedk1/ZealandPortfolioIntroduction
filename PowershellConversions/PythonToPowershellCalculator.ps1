# Simple Calculator in PowerShell

# Get user input
$num1 = Read-Host "Enter first number" | ForEach-Object { [double]$_ }
$num2 = Read-Host "Enter second number" | ForEach-Object { [double]$_ }
$op   = Read-Host "Choose operation (+, -, *, /)"

# Perform calculation
switch ($op) {
    '+' { $result = $num1 + $num2 }
    '-' { $result = $num1 - $num2 }
    '*' { $result = $num1 * $num2 }
    '/' {
        if ($num2 -ne 0) {
            $result = $num1 / $num2
        } else {
            $result = "Error: Division by zero"
        }
    }
    default { $result = "Invalid operation" }
}

Write-Host "Result: $result"
