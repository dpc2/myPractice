#!/bin/bash
#
# Verifying strings

echo $1

# Test whether first variable is empty
#test -z $1 && exit 1

# Using [[ ]] to check for specific pattern
[[ $1=='[a-z]*' ]] || echo $1 does not start with a letter
# This doesn't work for some reason?

exit 0

