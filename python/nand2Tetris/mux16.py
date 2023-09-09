str = '''    Not (in=a[0], out=nota#0#);
    Not (in=b[0], out=notb#0#);
    Not (in=sel, out=notsel);
    And (a=a[0], b=notb#0#, out=aAndnotb#0#);
    And (a=aAndnotb#0#, b=notsel, out=aAndnotbAndnotsel#0#);
    And (a=a[0], b=b[0], out=aAndb#0#);
    And (a=aAndb#0#, b=notsel, out=aAndbAndnotsel#0#);
    And (a=nota#0#, b=b[0], out=notaAndb#0#);
    And (a=notaAndb#0#, b=sel, out=notaAndbAndsel#0#);
    And (a=aAndb#0#, b=sel, out=aAndbAndsel#0#);
    Or (a=aAndnotbAndnotsel#0#, b=aAndbAndnotsel#0#, out=or1#0#);
    Or (a=notaAndbAndsel#0#, b=aAndbAndsel#0#, out=or2#0#);
    Or (a=or1#0#, b=or2#0#, out=out[0]);\n
'''

str0 = str.replace("#0#", "")
print(str0)


str1 = str.replace("[0]", "[1]")
str1 = str1.replace("#0#", "1")
print(str1)

str2 = str.replace("[0]", "[2]")
str2 = str2.replace("#0#", "2")
print(str2)

str3 = str.replace("[0]", "[3]")
str3 = str3.replace("#0#", "3")
print(str3)

str4 = str.replace("[0]", "[4]")
str4 = str4.replace("#0#", "4")
print(str4)

str5 = str.replace("[0]", "[5]")
str5 = str5.replace("#0#", "5")
print(str5)

str6 = str.replace("[0]", "[6]")
str6 = str6.replace("#0#", "6")
print(str6)

str7 = str.replace("[0]", "[7]")
str7 = str7.replace("#0#", "7")
print(str7)

str8 = str.replace("[0]", "[8]")
str8 = str8.replace("#0#", "8")
print(str8)

str9 = str.replace("[0]", "[9]")
str9 = str9.replace("#0#", "9")
print(str9)

str10 = str.replace("[0]", "[10]")
str10 = str10.replace("#0#", "10")
print(str10)

str11 = str.replace("[0]", "[11]")
str11 = str11.replace("#0#", "11")
print(str11)

str12 = str.replace("[0]", "[12]")
str12 = str12.replace("#0#", "12")
print(str12)

str13 = str.replace("[0]", "[13]")
str13 = str13.replace("#0#", "13")
print(str13)

str14 = str.replace("[0]", "[14]")
str14 = str14.replace("#0#", "14")
print(str14)

str15 = str.replace("[0]", "[15]")
str15 = str15.replace("#0#", "15")
print(str15)




##for i in range(0,15):
	##print(str.replace("[0]", ))

