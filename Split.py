#!/usr/bin/env python3.5

import sys,shlex
import os,errno,logging
import subprocess,urllib.request


class install:
    def __init__(self):
        self.LINK = None

    def check(self,LINK):
        #os.path.join(directory,'')
        LINK= 'https://'+LINK
        LINKCODE=urllib.request.urlopen(LINK).getcode()
        if LINKCODE == 200:
            print('Found the web page')

    def wget(self):
        command2="bash ./authentication.sh"
        command2=shlex.split(command2)
        subprocess.run(command2)
        return "I have installed wget"

    def download(self,LINK,bolum):
        com1="wget -O ./splitsfile/downloadedfile "+LINK
        com1=shlex.split(com1)
        subprocess.run(com1)
        com2="split -n "+str(bolum)+" ./splitsfile/downloadedfile ./splitsfile/"
        com2=shlex.split(com2)
        subprocess.run(com2)
        return "I have downloaded file"


class reunite:
    def __init__(self,directory):
        self.directory = directory

    def inputal(self):
        directory=input("you give me a path : ")
        os.path.join(directory,'')
        directory= directory+'*'
        return directory

    def command(self,directory):
        command = 'cat ' + directory + ' > orginalfile'
        try:
            subprocess.call[(command)]
        except Exception as e:
            raise
        return 'process complete!'

class ask:
    def __init__(self):
        self.bolum=None

    def pieces(self):
        bolum=-2
        while False == (( 0 <= int(bolum)) & (isinstance(bolum,int))):
            try:
                bolum=int(input("How many piece file: "))
                if int(bolum) <= 0:
                    raise ValueError
            except ValueError:
                logging.error('You should give meaningful a number: ')
            return bolum

    def split_on_file(self,bolum,PATH):
        command1="split -n"+str(bolum)+" "+PATH+" ./splitsfile/"
        command1=shlex.split(command1)
        subprocess.run(command1)

SORGU = ask()


__directory='./splitsfile'
answer=4

print("1-) Paste a web link.")
print("2-) Paste a file path")
print("3-) Paste a group file for reunion.")

while (answer != 2) & (answer != 1) & (answer != 3):
    try:
        answer=int(input('your choose:'))
    except ValueError:
        logging.error("you should give option.")


if answer==1:
    print("Your link should be www.example.com")
    LINK=input("link : ")
    INSTALL = install()
    try:
        INSTALL.check(LINK)
    except ConnectionError as e:
        print('Connection time out ', sys.exc_info()[0])
        exit()
    except:
        print('ERROR! Input should be: www.example.com')
        exit()
    try:
        if not os.path.exists(__directory):
            os.makedirs(__directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if not os.path.exists('/usr/bin/wget'):
        print('can you install wget? Y/N')
        WGET=str(input())
        if WGET=='Y':
            INSTALL.wget()
        else:
            print('you don\'t work this program.')
    bolum = SORGU.pieces()
    try:
        INSTALL.download(LINK,bolum)
    except OSError:
        print("Your os failure ")

if answer==2:
    PATH = str(input("can you give a path: ")).rstrip()
    try:
        if not os.path.exists(__directory):
            os.makedirs(__directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if os.path.isfile(PATH):
        try:
            bolum = SORGU.pieces()
            SORGU.split_on_file(bolum,PATH)
        except OSError:
            print('your os fauilure')
    else:
        print('please give me correct path!')


if answer == 3:
    calls = reunite('directory')
    DIR = calls.inputal()
    try:
        ZEP=calls.command(DIR)
    except:
        print("I didn't found directory. Problem is: ", sys.exc_info()[0])
