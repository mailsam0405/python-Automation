import os
import sys
def directoryfilesearch(dirname,ext):
        try:
            if os.path.isdir(dirname):
               for file in os.listdir(dirname):
                    if file.endswith(ext):
                       print(file)
            
            else:
                   print("invalid directory")
        except Exception as e:
            print("error:",e)   

def main():
   

     if len(sys.argv)!=3:
          print("files")
          return
     directoryfilesearch(sys.argv[1],sys.argv[2])                 
    

if __name__=="__main__":
    main()
