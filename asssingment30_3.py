#import os
#import sys
def main():
    fnmae=input("enter file name:")

    fobj=open(fnmae,"r")
    for i in fobj:
        print(i,end="")
    fobj.close()
    

if __name__=="__main__":
    main()
