#!/bin/bash

# Define the length of the password
LENGTH=16

# Generate a random password
PASSWORD=$(< /dev/urandom tr -dc 'A-Za-z0-9!@#$%^&*()_+{}|:<>?~' | head -c $LENGTH)

# Output the password
echo "Your random password is: $PASSWORD"
