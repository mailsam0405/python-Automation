import os
import sys
import hashlib
import time

def CalculateChecksum(Filename):
    fobj=open(Filename,"rb")
    hobj=hashlib.md5()
    
    Buffer=fobj.read(1000)
    while Buffer:
        hobj.update(Buffer)
        Buffer=fobj.read(1000)

    fobj.close()
    return hobj.hexdigest()

def DirectoryDuplicate(DirName):
    if not os.path.exists(DirName):
        print("This directory does not exists")
        return
    
    if not os.path.isdir(DirName):
        print("It is not a directory")
        return
    
    ChecksumDict={}

    logfile=open("Log.txt","w")
    logfile.write("Duplicate Files List\n")
    logfile.write("--------------------\n")

    for FolderName, Subfolder, FileName in os.walk(DirName):
        for fname in FileName:
            fullpath=os.path.join(FolderName,fname)
            checksum=CalculateChecksum(fullpath)

            if checksum in ChecksumDict:
                logfile.write(fullpath+"\n")
            else:
                ChecksumDict[checksum]=fullpath

    logfile.close()
    print("Duplicate files written to log.txt")

def main():
    start_time=time.time()

    if len(sys.argv) != 2:
        print("Usage : Automation32_2.py DirectoryName")
        return
        
    DirectoryDuplicate(sys.argv[1])
    end_time=time.time()
    print("Execution Time :",end_time-start_time,"seconds")

if __name__=="main_":
    main()