#------------------------------------------------#
#               2.6 - Self Check                 #
#------------------------------------------------#

#1. Big O performance? O(n^2)

n = 100

for i in range(n):
    for j in range(n):
        k = 2 + 2



#2. O(n)
for i in range(n):
    k = 2 + 2



#3 log2(n)
n = 100

i = n
count = 0
while i > 0:
    count += 1
    k = 2 + 2
    i = i // 2
    print(i)

print("Count = {}".format(count))



#4 O(n^3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            k = 2 + 2



#5 O(log(n))
i = n
while i > 0:
    k = 2 + 2
    i = i // 2



#6 O(n)
for i in range(n):
    k = 2 + 2
for j in range(n):
    k = 2 + 2
for k in range(n):
    k = 2 + 2