#import os
#import sys
def main():
    fnmae=input("enter file name:")

    fobj=open(fnmae,"r")
    count=0
    for  i in fobj:
        count=count+1
    fobj.close()

    
    print("total number of line",fnmae,":",count)

if __name__=="__main__":
    main()
