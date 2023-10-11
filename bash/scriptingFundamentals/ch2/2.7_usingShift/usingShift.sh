#!/bin/bash
#
# Script showing the use of shift

echo "The arguments provided are $*"
echo "The value of \$1 is $1"
echo "The entire string is $*"
echo -e "\n"

shift
echo "The new value of \$1 is $1"
echo "Now the entire string is $*"

exit 0

