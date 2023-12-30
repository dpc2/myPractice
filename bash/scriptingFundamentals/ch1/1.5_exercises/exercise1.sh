#!/bin/bash
# This script copies /var/log contents and clears current
# contents of the file
# Usage: ./exercise1.sh

cp /var/log/messages /var/log/messages.old
# rm /var/log/messages
cat /dev/null > /var/log/messages
echo log file copied and cleaned up

exit 0

