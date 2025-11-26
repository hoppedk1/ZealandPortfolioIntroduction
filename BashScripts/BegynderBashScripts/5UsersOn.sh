#!/bin/bash

# Count how many unique users are currently logged in
user_count=$(who | awk '{print $1}' | sort -u | wc -l)

echo "Number of unique users logged in: $user_count"

# If you want the total number of sessions (not just unique users), use this instead:
# session_count=$(who | wc -l)
# echo "Number of active login sessions: $session_count"
# Opgave 5
