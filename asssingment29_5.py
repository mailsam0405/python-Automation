import os
import sys
def main():
    fnmae=input("enter file name:")
    a=input("enter a string to search:")

    fobj=open(fnmae,"r")
    data=fobj.read()
    fobj.close()

    count=data.count(a)
    print(a,"appears",count,"times in",fnmae)

if __name__=="__main__":
    main()
