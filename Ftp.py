from ftplib import FTP
import gzip
import shutil
    
    
def inputDate():
    import datetime
    import calendar
    while True:
        day = input('Enter date[DD/MM/YYYY]:')
        try:
            day = datetime.datetime.strptime(day, "%d/%m/%Y")
            break
        except ValueError:
            print('Error: Accepted format DD/MM/YYYY')

    mon = calendar.month_abbr[int(day.month)]
    DMY = (f"{day.day}" + mon + f"{day.year}")
    return DMY


def AutoDate():
    from datetime import date
    today = date.today()
    mon = today.strftime("%b")
    DMY = today.strftime("%d" + mon + "%Y")
    return DMY

# DMY = AutoDate()
DMY = inputDate()

if DMY[1].isalpha():
    DMY = DMY.zfill(9)
else:
    pass


def ftpfile(DMY):
    ftp = FTP('ftp.connect2nse.com')
    ftp.login('FTPGUEST', 'FTPGUEST')

    path = '/Common/NTNEAT'
    ftp.cwd(path)

    try:
        # dir1 = input("enter path with / in front and back:")
        dir1 = "/home/nithin/Documents/sample/new/check/"

        fName1 = "contract.gz_" + DMY
        fName2 = "nnf_participant.gz_" + DMY
        fName3 = "nnf_security.gz_" + DMY
        fName4 = "participant.gz_" + DMY
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
    
        with open(pdir1, 'rb') as f_in:
            with gzip.open(dir1 + fName1 + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        with open(pdir2, 'rb') as f_in:
            with gzip.open(dir1 +fName2 + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        with open(pdir3, 'rb') as f_in:
            with gzip.open(dir1 +fName3 + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


        with open(pdir4, 'rb') as f_in:
            with gzip.open(dir1 +fName4 + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


        with open(pdir5, 'rb') as f_in:
            with gzip.open(dir1 +fName5 + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)


        with open(pdir6, 'rb') as f_in:
            with gzip.open(dir1 +fName6 + '.txt', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        print("Extracted!!!...")


    except:
        print("File not Found in FTP")


ftpfile(DMY)
