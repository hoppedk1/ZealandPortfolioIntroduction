#!/bin/bash

# Threshold in percent
THRESHOLD=10

# Get available percentage for root (/) filesystem
USAGE=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$USAGE" -ge $((100 - THRESHOLD)) ]; then
    echo "⚠️ Warning: Less than $THRESHOLD% disk space remaining!"
else
    echo "✅ Disk space is fine. $((100 - USAGE))% free remaining."
fi
