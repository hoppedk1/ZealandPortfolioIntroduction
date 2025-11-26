#!/bin/bash
user=$(whoami)
echo "running processes for $user : "
ps -u $user
