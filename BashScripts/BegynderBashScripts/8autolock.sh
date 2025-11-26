#!/bin/bash

# Time in minutes before lock
read -p "Enter time to autolock in minutes: " IDLE_TIME;

# The lock command (adjust depending on what locker you use)
LOCK_CMD="i3lock -c 000000"   # Example with i3lock, black background
#LOCK_CMD="xscreensaver-command -lock"   # Example with xscreensaver
#LOCK_CMD="gnome-screensaver-command -l" # Example for GNOME

# Run xautolock with idle timeout
echo "running autolock. remember to use ps and kill to turn it off again"
xautolock -time $IDLE_TIME -locker "$LOCK_CMD" &
#opgave 8
