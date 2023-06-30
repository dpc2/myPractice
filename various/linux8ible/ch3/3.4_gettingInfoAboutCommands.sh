#------------------------------------------#
# 3.4 - Getting Information about Commands #
#------------------------------------------#

# Check the PATH
echo $PATH

# Use the help command for info about
# built-in bash commands
help | less

# Use --help with the command
date --help | less
fdisk -h

# Use the info command
info date

# Use the man command
man date
# Use -k option to search the name and
# summary sections of all man pages 
man -k passwrd
# If man -k has no output, try initializing
# the man page database:
sudo mandb
# Selecting specific man page
man 5 passwd

