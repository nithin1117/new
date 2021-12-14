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
            print('Error: Invalid Date Format, Try DD/MM/YYY')
            sys.exit()

    mon = calendar.month_abbr[int(day.month)]
    dmy = (f"{day.day}" + mon + f"{day.year}")

if dmy[1].isalpha():
    dmy = dmy.zfill(9)
else:
    pass

    
def ftpfile(dmy, fName): 
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')
    path = '/Common/NTNEAT'
    ftp.cwd(path)


    try:
        key = 'FTPFILES'
        dir = os.getenv(key) + "/"
        # dir = "/home/nithin/Documents/sample/new/check/"

        pathDir = dir + fName
        ftp.retrbinary("RETR " + fName, open(pathDir, 'wb').write)
        ftp.close()
        
        with open(pathDir, 'rb') as f_in:
            with gzip.open(pathDir + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    except:
        print("File not found in FTP")
        return "error"


check = ftpfile(dmy, "contract.gz_" + dmy)

if check != "error":
    ftpfile(dmy, "nnf_participant.gz_" + dmy)
    ftpfile(dmy, "nnf_security.gz_" + dmy)
    ftpfile(dmy, "participant.gz_" + dmy)
    ftpfile(dmy, "security.gz")
    ftpfile(dmy, "spd_contract.gz")
    print("Downloaded and extracted!")
    
