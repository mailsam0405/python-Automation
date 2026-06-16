# Command line input
import psutil
import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.message import EmailMessage

# ------------------------ ZIP CREATION ------------------------------------
def make_zip(folder):
    timestamp=time.strftime("%Y-%m-%d_%H-%H-%S")
    zip_name=folder+"_"+timestamp+".zip"

    # open the zip file
    zobj=zipfile.ZipFile(zip_name,"w",zipfile.ZIP_DEFLATED)

    for root, dirs, files in os.walk(folder):
        for file in files:
            full_path=os.path.join(root,file)
            relative=os.path.relpath(full_path,folder)
            zobj.write(full_path,relative)

    zobj.close()

    return zip_name

# ------------------------ HASH CHECK ------------------------------------
def calculate_hash(path):
    hobj=hashlib.md5()

    fobj=open(path,"rb")

    while True:
        data=fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    fobj.close()

    return hobj.hexdigest()

# ------------------------ BACKUP FUNCTION ------------------------------------
def BackupFiles(Source, Destination):
    copied_files=[]
    print("creating the backup folder for backup process")

    os.makedirs(Destination,exist_ok=True)

    for root, dirs, files in os.walk(Source):
        for file in files:
            src_path=os.path.join(root,file)

            relative=os.path.relpath(src_path, Source)
            Dest_path=os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(Dest_path),exist_ok=True)

            # Copy the files if it's new
            if(not os.path.exists(Dest_path)) or (calculate_hash(src_path) != calculate_hash(Dest_path)):
                shutil.copy2(src_path, Dest_path)
                copied_files.append(relative)
            
    return copied_files

# ------------------------ EMAIL FUNCTION ------------------------------------
def send_mail(sender, app_passward, receiver, subject, body):
    msg=EmailMessage()
    msg["From"]=sender
    msg["To"]=receiver
    msg["Subject"]=subject

    msg.set_content(body)

    smtp=smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(sender, app_passward)

    smtp.send_message(msg)

    smtp.quit()

# --------------------- MAIN BACKUP PROCESS -----------------------------
def MarvellousDataShieldStart(Source="Data"):
    Border="-"*50
    
    BackupName="MarvellousBackup"

    print(Border)
    print("Backup process started successfully atb:",time.ctime())
    print(Border)

    files=BackupFiles(Source, BackupName)

    zip_file=make_zip(BackupName)


    # ✅ SEND MAIL AFTER BACKUP
    sender_email="152004.sanika@gmail.com"
    app_passward="hatgskcypldbkjyk"
    receiver_email="sanikamore.skncoe.comp@gmail.com"

    subject="Data Shield - Backup Completed Successfully"
    body = f"""
    Hello,

    The scheduled backup process has been completed successfully.

    Backup Details:
    ---------------------------
    Source Directory : {Source}
    Files Copied     : {len(files)}
    Zip File Created : {zip_file}
    Backup Time      : {time.ctime()}

    The system copied only newly added or modified files.

    Thank you for using Marvellous Data Shield.

    Regards,
    Marvellous Automation System
    """

    send_mail(sender_email, app_passward, receiver_email, subject, body)
    print("Mail Sent Successfully")

    print(Border)
    print("Backup completed successfully")
    print("Files Copied :",len(files))
    print("Zip file gets created :",zip_file)
    print(Border)

# ------------------------ MAIN FUNCTION ------------------------------------
def main():

    Border="-"*50
    print(Border)
    print("------------Marvellous Data Shield----------------")
    print(Border)

    if (len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to :")
            print("1 : Takes auto backup ata given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("Scriptname.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SounceDirectory : Name of directory to backup")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    # python Demo.py 5 Data
    elif (len(sys.argv)==3):
        print("Inside projects logic")
        print("TimeInterval :",sys.argv[1])
        print("DirectoryName :",sys.argv[2])
    
        # Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])

        print(Border)
        print("Data Shield System started successfully")
        print("Time interval in minutes :",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)

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