#------------------------------------------#
#   3.3 - Creating Your Shell Environment  #
#------------------------------------------#

#--- Configuring your shell ---#

# System-wide (sudo required):
/etc/profile
/etc/bashrc
# preferred method:
/etc/profile.d/custom.sh

# Individual user settings
~/.bash_profile
~/.bashrc
~/.bash_logout


#--- Setting your prompt ---#
PS1="\[\033[1;36m\][\$(date +%H%M)][\u@\h]:\[\033[1;32m\]\w\[\033[m\]$ "


#--- Adding environment variables ---#
TMOUT=30	# Close terminals after 30 seconds
