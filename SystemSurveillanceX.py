# Command line input
import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border="-"*50
    Ret=False
    Ret=os.path.exists(FolderName)

    if (Ret==True):
        Ret=os.path.isdir(FolderName)
        if (Ret==False):
            print("unabe to create folder")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for log Files gets created successfully")

    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName=os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name :",FileName)

    fobj=open(FileName,"w")
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Serveillance System------\n")
    fobj.write("log created at :"+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------System Report---------------------\n")

    #print("CPU usage :",psutil.cpu_percent())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem=psutil.virtual_memory()
    #print("RAM usage :",mem.percent)
    fobj.write("RAM Usage :%s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")
    for part in psutil.disk_partitions(all=False): # 'all=False' ignores virtual/non-physical
    # On Windows, try/except is often needed for CD-ROMs
        if 'cdrom' in part.opts or part.fstype == '':
            continue
        try:
            usage = psutil.disk_usage(part.device)   # ✅ use device, not mountpoint
            fobj.write("%s -> %s %% used\n" %(part.mountpoint,usage.percent))
        except (PermissionError, FileNotFoundError, OSError, SystemError):
            fobj.write(f"{part.device} -> Unable to access\n")
    fobj.write(Border+"\n")

    net=psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent / (1024 * 1024)))
    fobj.write("Recieve : %.2f MB\n" %(net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    # Process LOG
    Data=ProcessScan()

    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("Username : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("Start Time : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n" %info.get("memory_percent"))
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-------------End of log file ---------------------\n")
    fobj.write(Border+"\n")

def ProcessScan():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    # Warm up CPU percent
    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info=proc.as_dict(attrs=["pid","name","username","status","create_time"])
            # convert create_time
            try:
                info["create_time"]=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"])) 
            except:
                info["create_time"]="NA" 
            
            info["cpu_percent"]=proc.cpu_percent(None)
            info["memory_percent"]=proc.memory_percent()

            listprocess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listprocess

def main():

    Border="-"*50
    print(Border)
    print("-----Platform Serveillance System------")
    print(Border)

    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with logs")
            print("4 : Store information about processess")
            print("5 : Store information about CPU")
            print("6 : Store information about RAM usage")
            print("7 : Store information about secandary storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("Scriptname.py TimeInterval DirectoryName")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Marvellous
    elif (len(sys.argv)==3):
        print("Inside projects logic")
        print("TimeInterval :",sys.argv[1])
        print("DirectoryName :",sys.argv[2])
    
        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Serveillance System started successfully")
        print("Directory created with name :",sys.argv[2])
        print("Time interval in minutes :",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")


    print(Border)
    print("---------Thank you for using our Script-----------")
    print(Border)

if __name__=="__main__":
    main()