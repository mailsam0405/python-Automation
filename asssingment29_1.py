import os
def main():
    fnmae=input("enter file name:")
    if os.path.exists(fnmae):
        print("file is exsist")
    else:
        print("file is not exists")    

    
if __name__=="__main__":
    main()
