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
    dmy= AutoDate()

else:
    import datetime
    import calendar
    import sys

    while True:
        day = dmy
        try :
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


def ftpfile(dmy):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')

    path = '/Common/NTNEAT'
    ftp.cwd(path)

    try:
        
        key = 'FTPFILES'
        value = os.getenv(key)
        dir1 = value + "/"     
        
        #dir1 = "/home/nithin/Documents/sample/new/check/"

        fName1 = "contract.gz_" + dmy
        fName2 = "nnf_participant.gz_" + dmy
        fName3 = "nnf_security.gz_" + dmy
        fName4 = "participant.gz_" + dmy
        fName5 = "security.gz"
        fName6 = "spd_contract.gz"

        pdir1 = dir1 + fName1
        pdir2 = dir1 + fName2
        pdir3 = dir1 + fName3
        pdir4 = dir1 + fName4
        pdir5 = dir1 + fName5
        pdir6 = dir1 + fName6

        ftp.retrbinary("RETR " + fName1, open(pdir1, 'wb').write)
        ftp.retrbinary("RETR " + fName2, open(pdir2, 'wb').write)
        ftp.retrbinary("RETR " + fName3, open(pdir3, 'wb').write)
        ftp.retrbinary("RETR " + fName4, open(pdir4, 'wb').write)
        ftp.retrbinary("RETR " + fName5, open(pdir5, 'wb').write)
        ftp.retrbinary("RETR " + fName6, open(pdir6, 'wb').write)

        ftp.close()
        print("Downloaded")
        try:
            with open(pdir1, 'rb') as f_in:
                with gzip.open(pdir1[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(pdir2, 'rb') as f_in:
                with gzip.open(pdir2[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(pdir3, 'rb') as f_in:
                with gzip.open(pdir3[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(pdir4, 'rb') as f_in:
                with gzip.open(pdir4[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(pdir5, 'rb') as f_in:
                with gzip.open(pdir5[:-4] + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(pdir6, 'rb') as f_in:
                with gzip.open(pdir6[:-4] + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            print("Extracted!!!...")
        except:
            print("zip file path can't found")

    except :
        print("File not Found in FTP")


ftpfile(dmy)
