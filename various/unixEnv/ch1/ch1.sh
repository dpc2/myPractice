# 1.2 - Day to day use: files and common commands

# Bash commands

ls -lut
ls -lrt

# print files in an 8.5x11 format
pr -2 junk temp


# cat - named file(s) are "catenated"
# onto the terminal

cat junk temp



# ed - old screen editor

ed
a
Hullo World!
.
w junk
q

ed junk
19
1,$p	# Print lines 1 through last


# word count

# 8 lines, 46 words, 255 characters
wc poem


# grep - g/regular-expression/p
# v - invert

grep fleas poem
grep -v fleas poem


# sort
sort poem

sort -r     # Reverse order
sort -n     # Numeric order
sort -nr    # Reverse numeric
sort -f     # Fold upper, lower case
sort +n     # Sort starting at n+1


# tail - prints last 10 lines
tail -1 poem