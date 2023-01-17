string = "    Mux (a=a[0], b=b[0], sel=sel, out=out[0]);"


print(string);

for i in range(1,16):
	inc = str(i)
	strNew = string.replace("0", inc);
	print(strNew);


