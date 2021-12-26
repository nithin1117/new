from ftplib import FTP
import gzip
import shutil
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--date", help="name of the user")
args = vars(ap.parse_args())
dmy = args["date"]


def AutoDate():
    from datetime import date
    today = date.today()
    mon = today.strftime("%b")
    dmy = today.strftime("%d" + mon + "%Y")
    return dmy


if dmy == None:
    dmy = AutoDate()
else:
    import datetime
    import calendar
    import sys

    while True:
        day = dmy
        try:
            day = datetime.datetime.strptime(day, "%d/%m/%Y")
            break
        except ValueError:
            print('Error: Invalid Date Format, Try DD/MM/YYYY')
            sys.exit()

    mon = calendar.month_abbr[int(day.month)]
    dmy = (f"{day.day}" + mon + f"{day.year}")


if dmy[1].isalpha():
    dmy = dmy.zfill(9)
else:
    pass


def ftpfile(dmy):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')
    path = '/Common/NTNEAT'
    ftp.cwd(path)
    try:
        #key = 'FTPFILES'
        #dir = os.getenv(key) + "/"
        dir = "/home/nithin/dataCollect/trimData/test/src/script/files/"
        try:
            fName = [
                "contract.gz_" + dmy,
                "nnf_participant.gz_" + dmy,
                "nnf_security.gz_" + dmy,
                "participant.gz_" + dmy,
                "security.gz",
                "spd_contract.gz",
            ]
            for i in range(4):
                pathDir = dir + fName[i]
                ftp.retrbinary("RETR " + fName[i], open(pathDir, 'wb').write)
                

                with open(pathDir, 'rb') as f_in:
                    with gzip.open(pathDir[:-13]+ dmy + '.txt', 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                        
            for i in range(4, 6):
                pathDir = dir + fName[i]
                ftp.retrbinary("RETR " + fName[i], open(pathDir, 'wb').write)
                

                with open(pathDir, 'rb') as f_in:
                    with gzip.open(pathDir[:-3] + '.txt', 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
            ftp.close()

        except:
            print("Error: File not found for particular date in FTP")
            return "error"
    except:
        print("Error: path location had not prefered")
        print("run 'sudo gedit /etc/environment' and set 'FTPFILES = *desired directory*'")
        sys.exit()


check = ftpfile(dmy)

if check != "error":
    print("Downloaded and extracted!")
    
