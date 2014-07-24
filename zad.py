import time
length=-1
myA=-1
myB=-1
myC=-1
while length<0 or length>=100000:
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
	maxArg=-1
	minArg=-1
	if(arg1>=arg2):
		maxArg=arg1
		minArg=arg2
	else:
		maxArg=arg2
		minArg=arg1
	for i in range(minArg,maxArg):
		arr[i]=1	

ind=0
while ind<length:
	if((length-(ind+myC))%myB==0):
		change_arr(ind,ind+myC)
	if((length-(ind-myC))%myB==0):
		change_arr(ind,ind-myC)
	ind+=myA
result=0
for item in arr:
	if(item==0):
		result+=1
print result
end=time.clock()
print 'Run time is %4.2fs' % (end - start)

with open('result.html', 'wb') as outfile:
	print>>outfile,"""<html>
<head>
<title>Result</title>
</head>
<body>
with AY=%d a=%d b=%d c=%d Result is:%d
</body>
</html>""" % (length,myA,myB,myC,result)
