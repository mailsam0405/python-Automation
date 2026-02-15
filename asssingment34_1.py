import os
import sys
import zipfile
import shutil
import time
import smtplib
from email.message import EmailMessage

#Email
SENDER_EMAIL="itsmesam0405@gmail.com"
SENDER_PASSWARD="gmbnyzagmemsymiv"

#Logging Function
def write_log(message):
    os.makedirs("logs",exist_ok=True)
    logfile=os.path.join("logs","backup_log.txt")

    with open(logfile, "a") as f:
        f.write(message + "\n")

#Backup Function
def backup(source, exclude_ext):

    if not os.path.exists(source):
        print("Source folder does not exist")
        return
    
    timestamp=time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name=f"Backup_{timestamp}.zip"
    print("Creating zip file:", zip_name)

    write_log("-"*50)
    write_log("Backup Started at :"+time.ctime())

    file_count=0

    with zipfile.ZipFile(zip_name,"w") as zipf:
        for folder, subfolder, files in os.walk(source):
            for file in files:
                if any(file.endswith(ext) for ext in exclude_ext):
                    continue

                filepath=os.path.join(folder,file)
                zipf.write(filepath)
                file_count += 1

    write_log(f"files coppied : {file_count}")
    write_log(f"zip file created : {zip_name}")
    write_log("Bachup completed at : "+time.ctime())

    size=round(os.path.getsize(zip_name) / (1024 * 1024), 2)

    # Save history
    with open("Backup_history.txt","a") as history:
        history.write(f"{time.ctime()} | Files : {file_count} | Size: {size} MB\n")

    print("Backup Completed Successfully")
    send_mail(zip_name)

#Restore Function
def restore(zip_name, destination):

    if not os.path.exists(zip_name):
        print("zip file not found")
        return
    
    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zip_name,"r") as zipf:
        zipf.extractall(destination)

    print("Restore Completed successfully")

#Email Function
def send_mail(zip_name):

    try:
        msg=EmailMessage()
        msg["Subject"]="backup Completed"
        msg["From"]=SENDER_EMAIL
        msg["To"]=SENDER_EMAIL

        msg.set_content("Backup Completed Successfully. Log and Zip attached")

        # Attach zip file
        with open(zip_name,"rb") as f:
            msg.add_attachment(f.read(),maintype="application", subtype="octet-stream", filename=zip_name)

        # Attach Log file
        with open("logs/backup_log.txt","rb") as f:
            msg.add_attachment(f.read(),maintype="application", subtype="octet-stream", filename="Backup_log.txt")

        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWARD)
            smtp.send_message(msg)

        print("Email Sent Successfully")

    except Exception as e:
        print("Email Failed :",e)

# History Function
def show_history():
    if not os.path.exists("backup_history.txt"):
        print("No backup history found")
        return
    
    with open("backup_history.txt","r") as f:
        print(f.read())

#Main Function
def main():

    if len(sys.argv) < 2:
        print("Usage :")
        print("Backup   : python script.py FolderName")
        print("Restore  : python script.py --restore zipfile destination")
        print("History  : python script.py --history")
        return
    
    if sys.argv[1] == "--restore":
        restore(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "--history":
        show_history()

    else:
        source = sys.argv[1]
        exclude = [".tmp", ".log", ".exe"]
        backup(source, exclude)


if __name__ == "__main__":
    main()

