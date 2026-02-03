import os
def main():
    try:
        fnmae=input("enter file name:")
        fobj=open(fnmae)
        data=fobj.read()
        print(data)
        fobj.close()
        print("file get open")
    except FileNotFoundError:
        print("there is no search file")
if __name__=="__main__":
    main()
