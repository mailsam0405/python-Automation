#import os
#import sys
def main():
    fnmae=input("enter file name:")
    word=input("enter a word:")

    fobj=open(fnmae,"r")
    data=fobj.read()
    fobj.close()

    if word in data:
        print("word",word,"is found in",fnmae)
    else:
        print("word",word,"is not found in",fnmae)    
    

if __name__=="__main__":
    main()
