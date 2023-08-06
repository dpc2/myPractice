# Exercise 2-6
# Why does ls -li show 4 links for recipes?
# Hint: Try 'ls -ld /usr/you'
ls -li

# 4 links because recipes have 2 folders,
# 2 files in it



# Exercise 2-7
# Difference between:
mv junk junk1

# and
cp junk junk1
rm junk

# cp results in a file with the same contents,
# but different i-node



# Exercise 2-8
# cp doesn't copy subdirectories, only files at the first level of a hierarchy
# Unsure if cp -r existed back in the day, this question may not be relevant
