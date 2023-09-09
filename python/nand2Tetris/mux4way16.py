string = '''    Mux (a=a[%], b=b[%], sel=sel[0], out=aMuxb%);
    Mux (a=c[%], b=d[%], sel=sel[0], out=cMuxd%);
    Not (in=sel[1], out=notsel1%);
    And (a=aMuxb%, b=notsel1%, out=abOut%);
    And (a=cMuxd%, b=sel[1], out=cdOut%);
    Or (a=abOut%, b=cdOut%, out=out[%]);

'''


print(string);

for i in range(0,16):
	inc = str(i)
	strNew = string.replace("%", inc);
	print(strNew);


