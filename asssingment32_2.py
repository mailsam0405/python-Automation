import os
import sys
import hashlib

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
        print("This directory do not exists")
        return
    
    if not os.path.isdir(DirName):
        print("It is not a directory")
        return
    
    ChecksumDict={}

    logfile=open("log.txt","w")
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
    if len(sys.argv) != 2:
        print("Usage : Automation32_2.py DirectoryName")
        return
        
    DirectoryDuplicate(sys.argv[1])

if __name__=="main_":
    main()