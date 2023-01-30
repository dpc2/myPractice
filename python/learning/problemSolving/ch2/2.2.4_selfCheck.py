#------------------------------------------------#
#               2.2.4 - Self Check               #
#------------------------------------------------#

# Question 1: Big-O?
# Nested for-loops: O(n^2)

test = 0
n = 1 * (10 ** 100000)
n = 10

for i in range(n):
    for j in range(n):
        test = test + i *j



# Question 2: Big-O?
# Non-nested for-loops: O(2n) --> O(n)

test = 0
for i in range(n):
    test = test + 1

for j in range(n):
    test = test - 1



# Question 3: Big-O?
# O(log(n))

i = 100000000000
count = 0

while i > 0:
    k = 2 + 2
    i = i // 2
    print(i)
    count += 1

print('Loop count: {}'.format(count))

