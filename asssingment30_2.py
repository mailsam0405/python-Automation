#import os
#import sys
def main():
    fnmae=input("enter file name:")

    fobj=open(fnmae,"r")
    data=fobj.read()
    fobj.close()
    
    words=data.split()
    count=len(words)
    
    print("total number of line",fnmae,":",count)

if __name__=="__main__":
    main()
