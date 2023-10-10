#!/bin/bash
#
# Script showing the use of shift

echo "The arguments provided are $*"
echo "The value of \$1 is $1"
shift
echo "The new value of \$1 is $1"

exit 0

