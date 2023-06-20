!#/bin/bash
#------------------------------------------#
# 3.1 - Connecting and Expanding Commands
#------------------------------------------#

#--- Piping between commands ---#
# Metacharacters: has special meaning to the shell
# Examples: pipe character |, ampersand &, semicolon ;,
# left/right parenthesis (}, less/greater than < >

cat /etc/passwd | sort | less


# Contents of grep.1.gz are directed to the gunzip command to
# be unzipped, piped to the nroff command to format the man
# page using the manual macro (-man), then piped to less

gunzip < /usr/share/man/man1/grep.1.gz | nroff -c -man | less


#--- Sequential commands ---#
# Semicolons can be used to major sure commands complete
# before starting the next one

# This line uses date to time the runtime of a troff command
date ; troff -me verylargedocument | lpr ; date

# mail could be used to notify the user once a large command
# completes
mail -s "Finished the long command" burner.solo59@gmail.com
