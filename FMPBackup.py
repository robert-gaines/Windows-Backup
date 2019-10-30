#!/usr/bin/env python3

from multiprocessing import Process,freeze_support
from colorama import Fore,Style
from datetime import datetime
import colorama 
import shutil
import socket
import time
import sys
import os 

_auth_ = 'RWG'

'''
The purpose of this program is to copy a database file from
a local SMB to a Networked File Server
'''

def GenFileName():
    #
    n = datetime.now()
    #
    t = n.strftime("%m:%d:%Y - %H:%M:%S")
    #
    ts = n.strftime("%m_%d_%Y_%H_%M_%S")
    #
    backupFileName = "FMPDatabase_backup_"+ts+'.fmp12'
    #
    return backupFileName

def CheckFileServer():
    #
    print(Fore.YELLOW+"[*] Testing file server connectivity...") ; time.sleep(1)
    #
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #
    try:
        #
        conn_res = s.connect_ex(("129.101.113.51",445))
        #
    except:
        #
        print(Fore.RED+"[!] Socket Error [!]") ; time.sleep(1)
        #
        sys.exit(1)
        #
    finally:
        #
        s.close()
        #
    if(conn_res == 0):
        #
        print(Fore.GREEN+"[*] File Server Connection Test Passed [*]")
        #
        time.sleep(1)
        #
    else:
        #
        print(Fore.RED+"[!] File Server Connection Test Failed [!]")
        #
        time.sleep(1)
        #
        sys.exit(1)

def CheckLocalShare():
    #
    print(Fore.YELLOW+"[*] Checking for the presence of the local share...") ; time.sleep(1)
    #
    if(os.path.exists("\\\\129.101.89.245\\Documents\\FMP Database\\")):
        #
        print(Fore.GREEN+"[*] Located FMP Directory on Local Share [*]")
        #
        time.sleep(1)
        #
    else:
        #
        print(Fore.RED+"[!] Failed to locate local share [!]")
        #
        time.sleep(1)
        #
        sys.exit(1)

def CheckTargetDirectory():
    #
    print(Fore.YELLOW+"[*] Checking for the presence of the target directory...") ; time.sleep(1)
    #
    if(os.path.exists("\\\\129.101.113.51\\Shared\\SEM\\VA\\FMP Backups\\")):
        #
        print(Fore.GREEN+"[*] Located target directory on the network share [*]")
        #
        time.sleep(1)
        #
    else:
        #
        print(Fore.RED+"[!] Failed to locate target directory [!]")
        #
        time.sleep(1)
        #
        sys.exit(1)  

def main():
    #
    # Share IP Addr: 129.101.113.51
    # Share Directory: \\\\129.101.113.51\\Shared\\SEM\\VA\\FMP Backups\\
    # Host Directory: \\\\129.101.89.245\\Documents\\FMP Database\\
    #
    colorama.init(autoreset=True)
    #
    print(Fore.YELLOW+"[*] FMP Backup Utility [*]") ; time.sleep(1)
    #
    CheckLocalShare()
    CheckFileServer()
    CheckTargetDirectory()
    #
    sourceDir = "\\\\129.101.89.245\\Documents\\FMP Database\\"
    #
    dirlist = os.listdir("\\\\129.101.89.245\\Documents\\FMP Database\\")
    #
    backupTarget = "\\\\129.101.113.51\\Shared\\SEM\\VA\\FMP Backups\\"
    #
    targetFile = "" ; backupFile = GenFileName()
    #
    for d in dirlist:
        #
        if(d == 'FMPDatabaseforVeterans.fmp12'):
            #
            print(Fore.GREEN+"[*] Located the FMP Database: %s " % d)
            #
            targetFile = d
            #
    if(not targetFile):
        #
        print(Fore.RED+"[!] Failed to locate the FMP Database [!]") ; time.sleep(1)
        #
        sys.exit(1)
        #
    print(Fore.BLUE+"[~] Backup File Name-> %s " % backupFile)
    #
    print(Fore.YELLOW+"[*] Attempting the backup... ") ; time.sleep(1)
    #
    source = sourceDir+targetFile 
    #
    destination = backupTarget+backupFile
    #
    print(Fore.BLUE+"[*] Source: %s " % source) ; time.sleep(1)
    #
    print(Fore.BLUE+"[*] Destination: %s " % destination) ; time.sleep(1)
    #
    try:
        #
        shutil.copyfile(source,destination)
        #
        print(Fore.GREEN+"[*] Backup Operation Succeeded [*]") ; time.sleep(1)
        #
    except:
        #
        print(Fore.RED+"[!] Backup Operation Failed [!]") ; time.sleep(1)
        #
        sys.exit(1)
        #
    finally:
        #
        print(Fore.GREEN+"[*] Departing...") ; time.sleep(1)
    


if(__name__ == '__main__'):
    #
    freeze_support()
    #
    Process(target=main).start()
