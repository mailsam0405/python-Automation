import os
import sys
def main():
    if len(sys.argv)<3:
        pass
        return

    file1=sys.argv[1]
    file2=sys.argv[2]
    
    if os.path.exists(file1) and os.path.exists(file2): 
        fobj=open(file1,"r")
        data1=fobj.read()
        fobj.close()
        
        fobj2=open(file2,"r")
        data2=fobj2.read()
        fobj2.close()
        
        if data1==data2:
            print("sucsees")
        else:
            print("failuare")    
    else:
        
        print("there is no search file")
if __name__=="__main__":
    main()
