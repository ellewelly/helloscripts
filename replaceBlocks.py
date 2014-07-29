#!/usr/bin/python2
import sys,os
from string import strip,split,find


def fixFields(line, blockDict):
    (route,service,trip,headsign,block,shape) = line.split(",")

    # Filter out garages
    route = route.replace("-94","")
    route = route.replace("-84","")

    # Normalize service names
    if 'Weekend' in service:
        service="Weekend"
    elif 'Weekday' in service:
        service ="Weekday"

    # Replace blocks
    if block in blockDict:
        block = blockDict[block]
    else:
        pass

    return ','.join([route,service,trip,headsign,block,shape])


def setDictionary(blockReplFile):
    replaceLines = open(blockReplFile,'r').readlines()

    new_dict = {}
    for replaceLine in replaceLines:
        (key,value) = replaceLine.split(",")

        new_dict[key] = value.rstrip()

    return new_dict
         
def main():
    
    try :
        inFileName,replBlockFile, outFileName = sys.argv[1:]
        print inFileName
    except ValueError:
        print "Usage: messWithGTFS.py <inFileName> <block Replacement File> <outFileName>"
        sys.exit(2)

    
    blockDict = setDictionary(replBlockFile)
    #print blockDict

    
    inLines = open(inFileName,'r').readlines()
    outLines = open(outFileName,'w')

    print "Now going to read " + inFileName
    for line in inLines:
        fixLine = fixFields(line, blockDict)
        #print fixLine
        outLines.write(fixLine)
        
    outLines.close()
    print "CHANGES COMPLETE"

if __name__ == "__main__":
    main()


