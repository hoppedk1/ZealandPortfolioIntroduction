#!/bin/bash

# Path to monitor
file="/etc/passwd"

# Log file
log="/var/log/passwd_changes.log"

# State file to store last checksum
state="/var/tmp/passwd_checksum"

# Ensure log exists
sudo touch "$log"

# Get current checksum
current_sum=$(md5sum "$file" | awk '{print $1}')

# If no state file exists, create one
if [ ! -f "$state" ]; then
    echo "$current_sum" > "$state"
    echo "$(date): Initial checksum stored for $file" >> "$log"
    exit 0
fi

# Read old checksum
old_sum=$(cat "$state")

# Compare
if [ "$current_sum" != "$old_sum" ]; then
    echo "$(date): Change detected in $file" >> "$log"
    diff -u "$file" "$file.bak" >> "$log" 2>/dev/null
    # Update checksum
    echo "$current_sum" > "$state"
    # Save backup for future diffs
    cp "$file" "$file.bak"
fi
#opgave 1
