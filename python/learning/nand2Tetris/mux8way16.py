string = '''    Mux4Way16 (a=a[%], b=b[%], c=c[%], d=d[%], sel[0]=sel[0], sel[1]=sel[1], out=abcdMux%);
    Mux4Way16 (a=e[%], b=f[%], c=g[%], d=h[%], sel[0]=sel[0], sel[1]=sel[1], out=efghMux%);
    And (a=abcdMux%, b=notsel2, out=abcd%);
    And (a=efghMux%, b=sel[2], out=efgh%);
    Or (a=abcd%, b=efgh%, out=out[%]);
'''


print(string)
print("    Not (in=sel[2], out=notsel2);")

for i in range(0,16):
	inc = str(i)
	strNew = string.replace("%", inc)
	print(strNew)


