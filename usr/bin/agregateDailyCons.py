#!/usr/bin/python2.7
import time
from time import sleep
import datetime
import sys
import fnmatch
import os
import csv
#from datetime import datetime
#=========================================================================

# Definition des des variables temporelles
#=========================================================================
vHEURE = datetime.datetime.now().strftime('%H:%M:%S')
vDATE = datetime.datetime.today().strftime('%Y-%m-%d')
vCURRENTHOUR = datetime.datetime.now().strftime('%H')
vMONTH = datetime.datetime.today().strftime('%Y-%m') 
vDirLog = '/var/log/teleinfo/'
vListHCHP= []
for file in os.listdir(vDirLog):
    if fnmatch.fnmatch(file, "HCHC-HCHP*"):
        vHCFile = vDirLog+file
	
 	with open(vHCFile, 'rb') as csvfile:
	     	#spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		#print vHCFile
		firstline = csvfile.readline()
		rows = firstline.rstrip().split(',')
		#rows = list(csv.reader(csvfile, delimiter=',', quotechar='|'))
		#vLen = len(rows)
		#d = time.strptime(rows[0][0], "%Y-%m-%d %H:%M:%S")
		#day_string =  time.strftime("%Y-%m-%d",d)
		#print rows[0][0] + " , " +str(int(rows[vLen-1][1])- int(rows[0][1]))+" , " + str(int(rows[vLen-1][2])- int(rows[0][2]))
		dict = {'date':rows[0],'HC': int(rows[1]), 'HP': int(rows[2])}
		vListHCHP.append(dict)
		#for row in spamreader:
		#	print spamreader.line_num
		#	print row[1]
		#	print ', '.join(row)
vListHCHP.sort(key=lambda item:item['date'], reverse=False)
#print vListHCHP
vPreviousItem=None
print "date,HC,HP,Cumul"
for rows in vListHCHP:
	if vPreviousItem is not None:
		d = time.strptime(vPreviousItem['date'], "%Y-%m-%d %H:%M:%S")
                day_string =  time.strftime("%Y-%m-%d",d)
		vConsoHC = int(rows['HC'] - vPreviousItem['HC'])
		vConsoHP = int(rows['HP'] - vPreviousItem['HP'])
		print ""+day_string+ "," + str(vConsoHC) + "," +str(vConsoHP)+","+str(vConsoHC+vConsoHP)
	
	vPreviousItem = rows
