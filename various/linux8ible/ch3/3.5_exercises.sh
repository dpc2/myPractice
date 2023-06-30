#------------------------------------------#
# 	     3.5 - Exercises               #
#------------------------------------------#

#--- 1 ---#
# Switch to third virtual console, enter commands, exit


#--- 2 ---@
# Open a terminal, change font to red and background to yellow
PS1="\[\033[1;37m\]\[\033[0;40m\][\h][\w]$ \[\033[33m\]\[\033[41m\]"
PS1="\[$(tput setaf 15)\]\[$(tput setab 0)\][\h][\w]$ \[$(tput setaf 11)\]\[$(tput setab 9)\]" 


#--- 3 ---#
# Find mount
ls /bin | grep mount
# Find tracepath man page
man -k tracepath


#--- 4 ---#
# Type the following commands, then recall and edit them:
cat /etc/passwd
ls $HOME
date

cat /etc/group
ls -lt $HOME
date +%m/%d/%y


#--- 5 ---#
# Type the following using tab-completion
basena[TAB] /u[TAB]/sh[TAB]/doc/


#--- 6 ---#
cat /etc/services | less


#--- 7 ---#
mydate=$(date +"%A, %B %d, %Y.")
echo "Today is $mydate"


#--- 8 ---#
echo $HOSTNAME
echo $USERNAME
echo $SHELL
echo $HOME


#--- 9 ---#
alias mypass="cat /etc/passwd"


#--- 10 ---#
man mount
