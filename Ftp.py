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


def ftpfile(dmy):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')

    path = '/Common/NTNEAT'
    ftp.cwd(path)

    try:

        key = 'FTPFILES'
        dir1 = os.getenv(key) + "/"

        # dir1 = "/home/nithin/Documents/sample/new/check/"
        try:
            fName1 = "contract.gz_" + dmy
            fName2 = "nnf_participant.gz_" + dmy
            fName3 = "nnf_security.gz_" + dmy
            fName4 = "participant.gz_" + dmy
            fName5 = "security.gz"
            fName6 = "spd_contract.gz"

            ftp.retrbinary("RETR " + fName1, open(dir1 + fName1, 'wb').write)
            ftp.retrbinary("RETR " + fName2, open(dir1 + fName2, 'wb').write)
            ftp.retrbinary("RETR " + fName3, open(dir1 + fName3, 'wb').write)
            ftp.retrbinary("RETR " + fName4, open(dir1 + fName4, 'wb').write)
            ftp.retrbinary("RETR " + fName5, open(dir1 + fName5, 'wb').write)
            ftp.retrbinary("RETR " + fName6, open(dir1 + fName6, 'wb').write)

            ftp.close()
            with open(dir1 + fName1, 'rb') as f_in:
                with gzip.open(dir1 + fName1[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(dir1 + fName2, 'rb') as f_in:
                with gzip.open(dir1 + fName2[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(dir1 + fName3, 'rb') as f_in:
                with gzip.open(dir1 + fName3[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(dir1 + fName4, 'rb') as f_in:
                with gzip.open(dir1 + fName4[:-13] + dmy + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(dir1 + fName5, 'rb') as f_in:
                with gzip.open(dir1 + fName5[:-4] + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            with open(dir1 + fName6, 'rb') as f_in:
                with gzip.open(dir1 + fName6[:-4] + '.txt', 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

            print("Downloaded and Extracted!!!...")

        except:
            print("Error: File not found in FTP")
            return "error"
    except:
        print("Error: path location had not prefered")
        print("run 'sudo gedit /etc/environment' and set 'FTPFILES = /*desired directory*/'")
        sys.exit()


ftpfile(dmy)
