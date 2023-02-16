#------------------------------------------------#
#              2.1 - Basics of Files             #
#------------------------------------------------#

ed
.
a
now is the time
for all good people
.
w junk
q

# od - octal dump: visible representation of all bytes
# c - 'interpret bytes as characters'
# b - octal, base 8? <-- Hold over from PDP-11!
# x - hex
od -c junk


# cat -u: unbuffered
# cat is unbuffered by default now
cat -u