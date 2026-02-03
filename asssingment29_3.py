import os
import sys
def main():
    if len(sys.argv)<2:
        pass
        return

    fname=sys.argv[1]
    file="demo.txt"
    
    if os.path.exists(file): 
        fobj=open(file,"r")
        data=fobj.read()
        fobj.close()
        
        fobj2=open(fname,"w")
        fobj2.write(data)
        fobj2.close()
        
        print("file coped")
    else:
        
        print("there is no search file")
if __name__=="__main__":
    main()
