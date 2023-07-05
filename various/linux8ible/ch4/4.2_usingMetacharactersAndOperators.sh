#------------------------------------------#
#    Using Metacharacters and Operators    #
#------------------------------------------#

#--- Using file-matching metacharacters ---#
touch apple banana grape grapefruit watermelon
ls a*
ls g*
ls g*t
ls *e*
ls *n*

ls ????e
ls g???e*

ls [abw]*
ls [agw]*[ne]
ls [a-g]*


#--- Using file-redirection metacharacters ---#

# <: directs contents of a file to the standard input of a  command
# >: direct the standard output of a command to a file
# 2>: direct the standard error message to a file
# &>: direct both standard output and standard error
# >>: appends the output of a command to the end of a file

# Examples directing info from files
mail root < ~/.bashrc
man chmod | col -b > /tmp/chmod
echo "I finished the project on $(date)" >> ~/projects


# <<
# \'here text\' or \'here document\' allows text to
# be used as standard input for a command
mail root yangus itony pjimmy << thetext
"I want to tell everyone that there will be a 10am
meeting in the conference room B. Everyone should attend.

Love,
D
thetext

# Common use of here text: use it with a text editor to
# create or add to a file from a script:
/bin/ed /etc/resolv.conf <<resendit
a
nameserver 100.100.100.100
.
w
q
resendit



#--- Using brace expansion characters ---#

# Curly braces are used to expand a set of characters across
# filesnames, directory names, or other arguments to commands

# Ex: Create files memo1 through memo5:
touch memo{1,2,3,4,5}
ls

touch {Paul,John,George}-{Breakfast,Lunch,Dinner}
ls
rm -f {Paul,John,George}-{Breakfast,Lunch,Dinner}
touch {a..f}{1..5}
ls

