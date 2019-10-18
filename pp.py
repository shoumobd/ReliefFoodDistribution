import pymzn

my_solver=pymzn.CBC() #osicbc

child = pymzn.minizinc('project01c.mzn','d01c.dzn',solver=my_solver,output_mode='item')#,declare_enums=True)

l1 = child[0].split('\n')

#print(child)


with open("d01c.dzn", "r") as f:
    l = f.readlines()
for line in l:
	s = line.strip("\n")
	if s.startswith("childn"):
		cnum=int(''.join(filter(str.isdigit, s))) #number of children
		print("Number of children: ",cnum)
		ccnt=len(s)-8 #keeping the number of children and no. of digits of adultn which will be used for printing the 2d array output
		#print(ccnt)


for i in range(len(l1)):
	if l1[i].startswith("ap = "):
		op=l1[i]
		#print(op)
		op=op[ccnt+28:-3] #we'll print the distribution 2d array ap using string op starting from where the distribution values start
		#print(op)
		lp=op.split(',')
		#print(len(lp))
		print('\n\nCHILD PROTEIN DISTRIBUTION:\n\n\t',end='')
		for j in range(cnum):
			print('\tC',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(lp)):
			print(lp[j],'\t',end='')
			if j%cnum==cnum-1 and j+1<len(lp):
				print('\nITEM ',1+int((j+1)/cnum),':\t',end='')
		print('\n')
	if l1[i].startswith("ac = "):
		oc=l1[i]
		#print(oc)
		oc=oc[ccnt+25:-3] #we'll print the distribution 2d array ac using string oc starting from where the distribution values start
		#print(oc)
		lc=oc.split(',')
		#print(len(lc))
		print('\n\nCHILD CARB DISTRIBUTION:\n\n\t',end='')
		for j in range(cnum):
			print('\tC',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(lc)):
			print(lc[j],'\t',end='')
			if j%cnum==cnum-1 and j+1<len(lc):
				print('\nITEM ',1+int((j+1)/cnum),':\t',end='')
		print('\n')
	if l1[i].startswith("af = "):
		of=l1[i]
		#print(of)
		of=of[ccnt+26:-3] #we'll print the distribution 2d array af using string of starting from where the distribution values start
		#print(of)
		lf=of.split(',')
		#print(len(lf))
		print('\n\nCHILD FRUIT DISTRIBUTION:\n\n\t',end='')
		for j in range(cnum):
			print('\tC',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(lf)):
			print(lf[j],'\t',end='')
			if j%cnum==cnum-1 and j+1<len(lf):
				print('\nITEM ',1+int((j+1)/cnum),':\t',end='')
		print('\n')
	if l1[i].startswith("ad = "):
		od=l1[i]
		#print(od)
		od=od[ccnt+26:-3] #we'll print the distribution 2d array ad using string od starting from where the distribution values start
		#print(od)
		ld=od.split(',')
		#print(len(ld))
		print('\n\nCHILD DAIRY DISTRIBUTION:\n\n\t',end='')
		for j in range(cnum):
			print('\tC',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(ld)):
			print(ld[j],'\t',end='')
			if j%cnum==cnum-1 and j+1<len(ld):
				print('\nITEM ',1+int((j+1)/cnum),':\t',end='')
		print('\n')






for i in range(len(l1)):
	if l1[i].startswith("prornum"):
		sp=l1[i]
		#print(sp)
		sp1="pronum="+sp[27:-2]+";\n" #getting the updated protein units stock for the new dzn file
		#print(sp1) 
	if l1[i].startswith("carbrnum"):
		sc=l1[i]
		#print(sc)
		sc1="carbnum="+sc[25:-2]+";\n" #getting the updated carb units stock for the new dzn file
		#print(sc1)
	if l1[i].startswith("frnum"):
		sf=l1[i]
		#print(sf)
		sf1="fnum="+sf[23:-2]+";\n" #getting the updated fruit units stock for the new dzn file
		#print(sf1)
	if l1[i].startswith("drnum"):
		sd=l1[i]
		#print(sd)
		sd1="dnum="+sd[23:-2]+";\n" #getting the updated dairy units stock for the new dzn file
		#print(sd1)
	if l1[i].startswith("rbudget"):
		sb=l1[i]
		sb1=sb[1:]+"\n" #getting the updated remaining budget for the new dzn file
		#print(sb1)

	
with open("d01.dzn", "r") as f:
    l = f.readlines()
with open("d01.dzn", "w") as f:
	for line in l:
		s = line.strip("\n")
		if s.startswith("pronum="):
			continue
		if s.startswith("carbnum="):
			continue
		if s.startswith("fnum="):
			continue
		if s.startswith("dnum="):
			continue
		if s.startswith("budget"):
			continue
		f.write(line) #removing the old stocks from dzn file
		
		if s.startswith("adultn"):
			#anum=int(str(re.findall('\d+', "123")))
			anum=int(''.join(filter(str.isdigit, s))) #number of adults
			print("Number of adults: ",anum)
			acnt=len(s)-8 #keeping the number of adults and no. of digits of adultn which will be used for printing the 2d array output
			#print(acnt)

with open("d01.dzn", "a") as f:
	f.write(sp1) 
	f.write(sc1)
	f.write(sf1)
	f.write(sd1)
	f.write(sb1) #append the new stocks and budget at the end of the dzn file
		




adult = pymzn.minizinc('project01.mzn','d01.dzn',solver=my_solver,output_mode='item')

l2=adult[0].split('\n')

#print(adult)

for i in range(len(l2)):
	if l2[i].startswith("ap = "):
		op=l2[i]
		#print(op)
		op=op[acnt+28:-3] #we'll print the distribution 2d array ap using string op starting from where the distribution values start
		#print(op)
		lp=op.split(',')
		#print(len(lp))
		print('\n\nADULT PROTEIN DISTRIBUTION:\n\n\t',end='')
		for j in range(anum):
			print('\tA',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(lp)):
			print(lp[j],'\t',end='')
			if j%anum==anum-1 and j+1<len(lp):
				print('\nITEM ',1+int((j+1)/anum),':\t',end='')
		print('\n')
	if l2[i].startswith("ac = "):
		oc=l2[i]
		#print(oc)
		oc=oc[acnt+25:-3] #we'll print the distribution 2d array ac using string oc starting from where the distribution values start
		#print(oc)
		lc=oc.split(',')
		#print(len(lc))
		print('\n\nADULT CARB DISTRIBUTION:\n\n\t',end='')
		for j in range(anum):
			print('\tA',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(lc)):
			print(lc[j],'\t',end='')
			if j%anum==anum-1 and j+1<len(lc):
				print('\nITEM ',1+int((j+1)/anum),':\t',end='')
		print('\n')
	if l2[i].startswith("af = "):
		of=l2[i]
		#print(of)
		of=of[acnt+26:-3] #we'll print the distribution 2d array af using string of starting from where the distribution values start
		#print(of)
		lf=of.split(',')
		#print(len(lf))
		print('\n\nADULT FRUIT DISTRIBUTION:\n\n\t',end='')
		for j in range(anum):
			print('\tA',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(lf)):
			print(lf[j],'\t',end='')
			if j%anum==anum-1 and j+1<len(lf):
				print('\nITEM ',1+int((j+1)/anum),':\t',end='')
		print('\n')
	if l2[i].startswith("ad = "):
		od=l2[i]
		#print(od)
		od=od[acnt+26:-3] #we'll print the distribution 2d array ad using string od starting from where the distribution values start
		#print(od)
		ld=od.split(',')
		#print(len(ld))
		print('\n\nADULT DAIRY DISTRIBUTION:\n\n\t',end='')
		for j in range(anum):
			print('\tA',j+1,end='')
		print('\nITEM  1 :\t ',end='')
		for j in range(len(ld)):
			print(ld[j],'\t',end='')
			if j%anum==anum-1 and j+1<len(ld):
				print('\nITEM ',1+int((j+1)/anum),':\t',end='')
		print('\n')
		
		
		
