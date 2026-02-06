import os
import sys

def DirectoryRename(dirname,oldext,newext):
    if os.path.isdir(dirname):
        for file in os.listdir(dirname):
            if file.endswith(oldext):
                os.rename(
                    os.path.join(dirname,file),
                    os.path.join(dirname,file.replace(oldext,newext))

                )

    else:
        print("invalid dirctory")   

def main():
    if len(sys.argv)!=4:
          
          return
    
    DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])                 
    
    print("all file renmaed sucessfully")
    
if __name__=="__main__":
    main()

