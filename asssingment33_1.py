# Command line input
import psutil
import sys
import os
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime


def send_log_mail(sender, app_password, reciver, logfile):

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = reciver
    msg["Subject"] = "Marvellous Platform Surveillance Log"

    msg.set_content("Log file attached successfully")

    with open(logfile, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype="application",
                       subtype="octet-stream",
                       filename=os.path.basename(file_name))

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, app_password)
    smtp.send_message(msg)
    smtp.quit()

    print("Log mail sent successfully")


def CreateLogFolder(foldername):
    os.makedirs(foldername, exist_ok=True)


def GetLogFile(foldername):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    logfile = os.path.join(foldername, "Log_" + timestamp + ".txt")
    return logfile


def CollectProcessInfo():

    process_data = []

   
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(None)
        except:
            pass

    time.sleep(1)

    for proc in psutil.process_iter(
        ['pid', 'name', 'cpu_percent', 'memory_info',
         'memory_percent', 'num_threads', 'open_files']
    ):
        try:
            info = proc.info

            rss = info['memory_info'].rss if info['memory_info'] else 0
            vms = info['memory_info'].vms if info['memory_info'] else 0
            open_files = len(info['open_files']) if info['open_files'] else 0

            entry = (
                "Process Name : " + str(info['name']) + "\n"
                "PID          : " + str(info['pid']) + "\n"
                "CPU %        : " + str(info['cpu_percent']) + "\n"
                "Memory %     : " + format(info['memory_percent'], ".2f") + "\n"
                "RSS          : " + str(rss) + "\n"
                "VMS          : " + str(vms) + "\n"
                "Threads      : " + str(info['num_threads']) + "\n"
                "Open Files   : " + str(open_files) + "\n"
                "Timestamp    : " + str(datetime.now()) + "\n"
                + "-" * 50 + "\n"
            )

            process_data.append(entry)

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return process_data


def WriteLog(data, logfile):
    with open(logfile, "w") as f:
        for entry in data:
            f.write(entry)


def PlatformSurveillanceStart(foldername, reciver):

    Border = "-" * 50

    print(Border)
    print("Platform Surveillance started at :", time.ctime())
    print(Border)

    CreateLogFolder(foldername)

    logfile = GetLogFile(foldername)

    data = CollectProcessInfo()
    WriteLog(data, logfile)

    sender_email = "itsmesam0405@gmail.com"
    app_password = "gmbnyzagmemsymiv"

    send_log_mail(sender_email, app_password, reciver, logfile)

    print(Border)
    print("Log file created :", logfile)
    print("Surveillance cycle completed")
    print(Border)


def main():

    Border = "-" * 50
    print(Border)
    print("-----------Marvellous Platform Surveillance-----------")
    print(Border)

    if (len(sys.argv) == 2):

        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is used to :")
            print("1 : Monitor running processes")
            print("2 : Store process log into file")
            print("3 : Send log file via email periodically")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of script :")
            print('python PlatformSurveillance.py "LogFolderName" "ReceiverEmail" TimeInterval')

        else:
            print("Unable to proceed as there is no such option")
            print("Use --h or --u for help")

    elif (len(sys.argv) == 4):

        foldername = sys.argv[1]
        reciver = sys.argv[2]
        interval = int(sys.argv[3])

        print("Starting surveillance with interval :", interval, "seconds")
        print("Press Ctrl + C to stop")

        while True:
            PlatformSurveillanceStart(foldername, reciver)
            time.sleep(interval)

    else:
        print("Invalid number of command line arguments")
        print("Use --h or --u for help")

    print(Border)
    print("---------Thank you for using our Script-----------")
    print(Border)


if __name__ == "__main__":
    main()
