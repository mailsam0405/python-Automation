#import os
#import sys
def main():
    fnmae1=input("enter file name:")
    fname2=input("enter second file name:")

    fobj=open(fnmae1,"r")
    data=fobj.read()
    fobj.close()

    fobj2=open(fname2,"w")
    fobj2.write(data)
    fobj2.close()

    print("contents of",fnmae1,"copied into",fname2)

if __name__=="__main__":
    main()
