import time
length=-1
myA=-1
myB=-1
myC=-1
while length<0 or length>=1000000:
	length=int(input("AY="))
while myA<0 or myA>=100000:
	myA=int(input("a="))
while myB<0 or myB>=100000:
	myB=int(input("b="))
while myC<0 or myC>=100000:
	myC=int(input("c="))

start=time.clock()
arr=[0]*length

def change_arr(arg1,arg2):
	maxArg=arg2
	minArg=arg1
	for i in range(minArg,maxArg):
		arr[i]=1	

ind=0
while ind<length:
	if((length-(ind+myC))%myB==0 and ind+myC<=length):
		change_arr(ind,ind+myC)
	if((length-(ind-myC))%myB==0 and ind-myC>=0):
		change_arr(ind-myC,ind)
	ind+=myA
result=0
for item in arr:
	if(item==0):
		result+=1
print result
print 'Run time is %4.2fs' % (time.clock() - start)

with open('result.html', 'wb') as outfile:
	print>>outfile,"""<html>
<head>
<title>Result</title>
</head>
<body>
"""
	bold=False
	wasBold=False
	if arr[0]:
		bold=True
	for i in range(0,len(arr)):
		if arr[i]:
			bold=True
		else:
			if(i>0 and arr[i-1]):
				wasBold=True
			bold=False
		if bold or wasBold:
			print>>outfile, "<text style='color:#ff0000;'>",i,"</text> ",
			if wasBold:
				wasBold=False
		else:
			print>>outfile, i," ",
		
	if bold or wasBold:
		print>>outfile, "<text style='color:#ff0000;'>",len(arr),"</text> ",
	else:
		print>>outfile, len(arr)," ",
	print>>outfile, "<hr></body></html>"
