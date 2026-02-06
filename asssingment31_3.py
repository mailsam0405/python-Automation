import os
import sys

def Directorycopy(src,dest,ext):
     if not os.path.isdir(src):
          print("invalid source directory")
          return
     
     if not os.path.exists(dest):
          os.mkdir(dest)

          for file in os.listdir(src):
               if file.endswith(ext):
                    src_file=os.path.join(src,file)
                    dest_file=os.path.join(dest,file)

                    f1=open(src_file,"r")
                    data=f1.read()
                    f1.close()

                    f2=open(dest_file,"w")
                    f2.write(data)
                    f2.close()
   
def main():
    if len(sys.argv)!=4:
        
          return
    
    Directorycopy(sys.argv[1],sys.argv[2],sys.argv[3])                 
    print("all file coped successfully")
    
    
if __name__=="__main__":
    main()

