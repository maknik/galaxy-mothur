#!/usr/bin/env python
import sys, subprocess
tmp=[]
n=int(sys.argv[2])
if n < 1: n=1
i=1
for line in open(sys.argv[1]):
	if line.split('"')[0]=='<a href=':
		if i==n:
			proc2 = subprocess.Popen("pwd", shell=True, stdout=subprocess.PIPE)
			pwd=proc2.stdout.read()
			pwd=pwd.split('/')[1]+'/'+pwd.split('/')[2]+'/'+pwd.split('/')[3]
			cmdline= "find /"+pwd+" -name "+line.split('"')[1]
			proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
			filename=proc.stdout.read().split('\n')[0]
			filen=open(filename)
			for line in filen:
				tmp.append(line)
			break
		else: i+=1
				
out=open(sys.argv[4], 'w')
if sys.argv[3]=='yes':
	for i in tmp[1:]:
		out.write(i)
else: 
	for i in tmp: 
		out.write(i)
