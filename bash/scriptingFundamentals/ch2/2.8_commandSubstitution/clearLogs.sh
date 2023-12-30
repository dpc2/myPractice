#!/bin/bash
#
# This script copies /var/log contents and clears the
# current contents of the file
# Usage: ./clearLogs

cp /var/log/messages /var/log/messages.$(date +%d-%m-%y)
cat /dev/null > /var/log/messages

echo log file copied and cleaned up

exit 0

