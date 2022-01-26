from ftplib import FTP
import gzip
import shutil
import argparse
import os
from ftplib import error_perm

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


if dmy is None:
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


def ftpFile(dmy):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')
    path = '/Common/NTNEAT'
    ftp.cwd(path)
    try:
        # key = 'FTPFILES'
        # dir = os.getenv(key) + "/"
        dir = "D:/New1folder/"

        fName = [
            "contract.gz_" + dmy,
            "nnf_participant.gz_" + dmy,
            "nnf_security.gz_" + dmy,
            "participant.gz_" + dmy,
            "security.gz_" + dmy,
            "spd_contract.gz_" + dmy,
        ]

        for i in range(6):
            pathDir = dir + fName[i]
            ftp.retrbinary("RETR " + fName[i], open(pathDir[:-10], 'wb').write)

            with gzip.open(pathDir[:-10], 'rb') as f_in:
                with open(pathDir[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

        ftp.close()
        print(f"Downloaded and extracted for date: {dmy}")

    except error_perm as msg:
        print(f"File not found for particular date: {dmy}")

    except:
        print("Error Occurred, check the path directory")
        print("run 'sudo gedit /etc/environment' and set 'FTPFILES = *desired directory*'")


ftpFile(dmy)

