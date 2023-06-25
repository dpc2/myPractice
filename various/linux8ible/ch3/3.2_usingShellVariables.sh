#------------------------------------------#
#	 3.2 - Using Shell Variables       #
#------------------------------------------#
# Example variables:
$SHELL
$PS1
$MAIL

# List of variables for current shell:
set
# A subset: environment variables
env
# Current env variables and shell functions
declare

echo $USER


#--- Creating and using aliases ---#
# List aliases
alias
unalias

alias p='pwd ; ls -CF'
alias rm='rm -i'


#--- Exiting the shell ---#
exit
Ctrl+D

