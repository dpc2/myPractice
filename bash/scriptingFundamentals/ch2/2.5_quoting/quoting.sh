#!/bin/bash
#
# Quoting

echo The value of the $PATH variable is $PATH

echo The value of the \$PATH variable is $PATH

echo 'The value of the $PATH variable is $PATH'

echo 2 * 3 > 5
echo '2 * 3' > 5

echo "The value of the \$PATH variable is $PATH"

# Best practice: Use single quotes unless you specifically need parameter,
# command, or arithmetic substituion

