#!/usr/bin/python
#http://api.sba.gov/doc/license_permit.html

__author__ = 'epalmer'
import urllib2, os, sys, fileinput

print "Getting and Saving State Data"

'''
dataFolder = './data/output/sba/state/'
root = "http://api.sba.gov/geodata/city_county_data_for_state_of/"

for line in fileinput.input(['./data/input/stateCodes']):
    state = line.rstrip('\n').split(',')[0]
    code = line.rstrip('\n').split(',')[1]
    print "Processing " + state
    folder = dataFolder + state
    if not os.path.exists(folder): os.makedirs(folder)
    url = root + code
    print url
    response = urllib2.urlopen(url)
    responseBody = response.read()
    #print responseBody
    # write the file
    # Open a file
    file = folder + "/" + code + ".xml"
    fo = open(file, "w")
    fo.write(responseBody)
    fo.close()
"Print done processing files"
'''

print "Getting and Saving Zipcode Data"

dataFolder = './data/output/sba/zip/'
#http://api.sba.gov/license_permit/by_zip/child%20care%20services/90210.xml
root = "http://api.sba.gov/license_permit/by_zip/"

for line in fileinput.input('./data/input/zipcode.txt'):
    zip = line.rstrip('\n')

    folder = dataFolder + zip[:3]
    if not os.path.exists(folder): os.makedirs(folder)
    for bustype in fileinput.FileInput('./data/input/busType'):
        busType = bustype.rstrip('\n')
        busTypeEnc = urllib2.quote(busType)
        url = root + busTypeEnc +  "/" + zip + ".xml"
        print url
        response = urllib2.urlopen(url)
        responseBody = response.read()
        #print responseBody
        # write the file
        # Open a file
        file = folder + "/" + busType + "_" + zip + ".xml"
        fo = open(file, "w")
        fo.write(responseBody)
        fo.close()
"Print done processing files"