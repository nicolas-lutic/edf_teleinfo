#!/usr/bin/python2.7
import time
from time import sleep
import datetime
import sys
import fnmatch
import os
import csv
#from datetime import datetime
import ConfigParser
config = ConfigParser.RawConfigParser()

print config.read('/etc/house-on-wire/house-on-wire.ini')
print config.sections()

# get sensor list from ini
vListSensor =  config.options('sonde-temp')

#configDict = {section:{option:config.get(section,option) for option in config.options(section)} for section in config.sections()}
#print configDict['sonde-temp']

#=========================================================================

# Definition des des variables temporelles
#=========================================================================
vHEURE = datetime.datetime.now().strftime('%H:%M:%S')
vDATE = datetime.datetime.today().strftime('%Y-%m-%d')
vCURRENTHOUR = datetime.datetime.now().strftime('%H')
vMONTH = datetime.datetime.today().strftime('%Y-%m') 
vDirLog = '/var/log/1wire/temperature/'
for file in os.listdir(vDirLog):
    
	for SensorName in vListSensor: 
		SensorName = SensorName.upper()
		#print SensorName
		if fnmatch.fnmatch(file, SensorName+'-*'):
        		vHCFile = vDirLog+file
			print file.split('-')
			print SensorName
 			with open(vHCFile, 'rb') as csvfile:
	     			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
				#print spamreader[0]
				spamreader.sort(key=lambda item:item[0], reverse=False)
				print spamreader
#print "date,temp"
#for rows in vListHCHP:
#	d = time.strptime(vPreviousItem['date'], "%Y-%m-%d %H:%M:%S")
#        day_string =  time.strftime("%Y-%m-%d",d)
#	vConsoHC = int(rows['temp'] )
#	print ""+day_string+ "," + str(vConsoHC) + "," +str(vConsoHP)+","+str(vConsoHC+vConsoHP)
	
