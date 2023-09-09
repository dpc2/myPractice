#------------------------------------------------#
#                  Ch. 16 - Bash                 #
#------------------------------------------------#


echo Hello, World!

# Recent commands
history

# Relative/Absolute paths
/home/danny/downloads/

# Navigating
cd /home/danny/downloads/
pwd

# Flags - Set to False by default, can be set True
# by using "-" or "--" followed by the flag to set
cd ~/code/python/selfTaught/ch16/
ls -author

# Hidden files
touch .self_taught
ls -a
cd /home/danny/downloads/
ls | less

# Environmental variables
export x=100
echo x equals $x

# Users
whoami