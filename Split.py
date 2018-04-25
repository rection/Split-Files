#!/bin/python

import subprocess,sys
import os,errno,logging

class Control:
    def __init__(self,bolum):
        if not (1 < bolum) & (4 <= sys.getsizeof(bolum)) & (sys.getsizeof(bolum) < 40):
            print('you should be give meaningful number.')

__directory='./splitsfile'
answer=4
bolum=5
print("1-) First You should paste the link, thereafter downloaded file does exist four piece.")
print("2-)if you have a file and you want file to four piece.")
while (answer != 2) & (answer != 1):
    try:
        answer=int(input('your choose:'))
    except ValueError:
        logging.error("you should give option.")
        
while True ==(( 0 <= int(bolum)) & (isinstance(bolum,int))):            
    try:
        bolum=input("Should how many piece file: ")
        if int(bolum) <= 0:
            raise ValueError
    except ValueError:
        logging.error('You should give meaningful a number: ')

            

if answer==1:
    LINK=input("link : ") #try catch ata giriyi duzgun atadi mi?
    try:
        if not os.path.exists(__directory):
            os.makedirs(__directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    if not os.path.exists('/bin/wget'):
        print('can you install wget? y/n')
        WGET=str(input())
        if WGET==y:
            print('you do it yourself!')
        else:
            print('you don\'t work this program.')
    try:
        subprocess.call(['wget','-O','./splitsfile/downloadedfile',LINK])
        subprocess.call(['split','-n',bolum,'./splitsfile/downloadedfile','./splitsfile/'])
    except OSError:
        print("Your os failure ")
        
if answer==2:
    
    PATH=str(input('can you give a path: ')).rstrip()
     
    try:
        if not os.path.exists(__directory):
            os.makedirs(__directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        
    if os.path.isfile(PATH):
        try:
            subprocess.call(['split','-n',bolum, PATH ,'./splitsfile/'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        except OSError:
            print('your os fauilure')
    else:
        print('please give me correct path!')

