#!/usr/bin/env python

# author: greyshell
# description: finding safe ppr address 
# dependency: seh.txt generated from mona.py, goodchars.txt generated from automated barchars detection script

import sys
import os

flag = 0
count = 0

def testSafeChar(ch,safestring):
	global flag
	global count
	
	p = safestring.find(ch)
	if p <= 0:
		flag = 0
	else:
		flag = 1
		count = count + 1 
	
	return
	
def main():
	
	global flag
	global count
	notFound = 'true'
	
	if len(sys.argv) != 3:
		print "[*] Usage: finding-safe-ppr.py <seh.txt> <goodchars.txt>"
		sys.exit(0)
		
	fseh = sys.argv[1]
	fsafe = sys.argv[2]

	try:
		# processing goodchars.txt
		with open(fsafe, "r") as in_file:						
			for safestring in in_file:
				pass
				
		# processing seh.txt
		with open(fseh, "r") as in_file:			
			flag = 0			
			for line in in_file:
				addr = line[0:10]
				
				c1 = addr[2:4]
				testSafeChar(c1,safestring)
				
				c2 = addr[4:6]
				testSafeChar(c2,safestring)
				
				c3 = addr[6:8]
				testSafeChar(c3,safestring)
				
				c4 = addr[8:10]
				testSafeChar(c4,safestring)
				
				if count == 4:
					print line
					print 
					notFound = 'false'
					
				count = 0
		
		in_file.close()	
		
		if notFound == 'true':
			print '[+] Not found any bad char friendly ppr address from seh.ext'


	except Exception as e:
		print e
	else:
		pass
	
	finally:
		pass
		

if __name__ == '__main__':
	main()
