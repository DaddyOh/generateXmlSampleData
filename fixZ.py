#!/usr/bin/python

#http://www.unitedstateszipcodes.org/zip-code-database/

import fileinput, os

__author__ = 'epalmer'


print (os.getcwd(), "\n");
outfile = "./data/input/zipcode.txt"
fo = open(outfile, "w")
count = 0
threeDigitOrg = ""
threeDigit = ""
count3 = 0

for line in fileinput.input('./data/input/zipcode.bad'):
    count += 1
    zip = line.rstrip('\n')
    if len(zip) <5:
        zip = zip.rjust(5, '0')

    fo.write(zip + "\n")
    threeDigit = zip[:3]
    if threeDigit != threeDigitOrg:
        threeDigitOrg = threeDigit
        count3 = count3 + 1
fo.close()
msg = str(count) + " zipcode values in " + outfile
print msg
msg = str(count3) + " 3 digit values of zip"
print msg
