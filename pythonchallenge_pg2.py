s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

snew = "map"
lista = list(s);
#print(lista)
b = ""
for ch in snew:
	if ord(ch) == 121 : 
		a = chr(ord(ch) -24)
		#print("the valu of y is" , a);
		b+=str(a)
	elif ord(ch) == 122 : 
		a = chr(ord(ch) -24)
		#print("the valu of z is" , a);
		b+=str(a)
	elif ord(ch) > 96 and ord(ch) < 121:
		a = chr(ord(ch) + 2)
		#print("current value is" , a);
		b+=str(a)
	
		
	
#print(listb)

#str1 = ''.join(listb)
print(b)