#!/usr/bin/env python3

import shutil
import psutil
import time
import sys
import os

time = time.ctime()
#
sansSpaces =  time.replace(' ','_',4)
#
refinedTime = time.replace(':','',2)
#
user = os.getlogin()
#
filename = "C:\\Users\\"+user+"\\Desktop\\"+"BackupTranscript"+"_"+refinedTime+".txt"
#
transcript = open(filename,'w')

def selectDisk():
    #
    diskList = []
    #
    disks = psutil.disk_partitions()
    #
    options = []
    #
    print("""
    Disk \t Mount Point \t File System Type \t Percent Used 
    ---- \t ----------- \t ---------------- \t ------------
           """)
    #
    for i in range(0,len(disks)):
        #
        entry = []
        #
        disk  = disks[i][0]
        mount = disks[i][1]
        fs    = disks[i][2]
        #
        utilization = psutil.disk_usage(disk)
        #
        percentUsed = utilization.percent
        #
        entry.append(disk)
        entry.append(mount)
        entry.append(fs)
        #
        print(i,')',disk,'\t',mount,'\t\t',fs,'\t\t\t',percentUsed,'\t')
        #
        diskList.append(entry)
        #
    print('\n')
    #
    selection = int(input("[+] Enter the disk index-> "))
    #
    return diskList[selection]

def backupFiles(rootDirectory,backupDestination):
    #
    for directory,subDirectory,fileList in os.walk(rootDirectory):
        #
        print("[*] Located directory: %s " % directory)
        #
        transcript.write("%s - Located directory: %s \n" % (refinedTime, directory))
        #
        transcript.write("%s - Located sub-directory: %s \n" % (refinedTime, subDirectory))
        #
        for s in subDirectory:
            #
            transcript.write("\t\t\t Located subdirectory: %s \n" % s) 
            #
        for f in fileList:
            #
            transcript.write("%s - Located file: %s \n" % (refinedTime, f))
            #
            #print("\t\t\t\t[*] Located file: %s " % f)
            #
        try:
            #
            print("[*] Backing up: %s " % directory)
            #
            transcript.write("%s - Backed up directory: %s \n" % (refinedTime, directory))
            #
            shutil.copytree(directory,backupDestination,symlinks=False)
            #
        except:
            #
            pass
            
        
def main():
    #
    print('''
     ______   _______  _______  _                 _______          
    (  ___ \ (  ___  )(  ____ \| \    /\|\     /|(  ____ )         
    | (   ) )| (   ) || (    \/|  \  / /| )   ( || (    )|         
    | (__/ / | (___) || |      |  (_/ / | |   | || (____)|         
    |  __ (  |  ___  || |      |   _ (  | |   | ||  _____)         
    | (  \ \ | (   ) || |      |  ( \ \ | |   | || (               
    | )___) )| )   ( || (____/\|  /  \ \| (___) || )               
    |/ \___/ |/     \|(_______/|_/    \/(_______)|/                
                                                                   
             __________________ _       __________________         
    |\     /|\__   __/\__   __/( \      \__   __/\__   __/|\     /|
    | )   ( |   ) (      ) (   | (         ) (      ) (   ( \   / )
    | |   | |   | |      | |   | |         | |      | |    \ (_) / 
    | |   | |   | |      | |   | |         | |      | |     \   /  
    | |   | |   | |      | |   | |         | |      | |      ) (   
    | (___) |   | |   ___) (___| (____/\___) (___   | |      | |   
    (_______)   )_(   \_______/(_______/\_______/   )_(      \_/   
                                                               
          ''')
    #
    currentUser = os.getlogin()
    #
    operatingSystem = os.name
    #
    netAdapter = psutil.net_if_addrs()
    #
    ip = netAdapter['Ethernet'][1][1]
    #
    print("\n")
    #
    print("Backup operation started at: %s " % refinedTime)
    #
    transcript.write("Backup operation started at: %s \n" % refinedTime)
    #
    print("---------------------------\n")
    #
    transcript.write("---------------------------\n")
    #
    transcript.write('''
    Current User: %s \n                   
    IP Address:   %s \n
    OS Type:      %s \n
                     ''' % (currentUser, ip, operatingSystem))
    #
    transcript.write("\n")
    #
    print('''
    Current User: %s                    
    IP Address:   %s
    OS Type:      %s
          ''' % (currentUser, ip, operatingSystem))
    #
    backupDisk = selectDisk()
    #
    transcript.write("%s - User selected disk: %s \n" % (refinedTime,backupDisk))
    #
    backupTarget = str(backupDisk[0])+"Backup"+"_"+refinedTime
    #
    userDir = "C:\\Users\\"+currentUser
    #
    print("[*] Backup target is: %s " % userDir)
    #
    transcript.write("%s - Backup target set as: %s \n" % (refinedTime,userDir))
    #
    print('''
    **************************************************************************
    *** Program will close automatically when backup operation is complete ***
    **************************************************************************
          ''')
    #
    backupFiles(userDir,backupTarget)
    #
    print("[*] Backup Complete - Departing [*]")
    #
    transcript.write("%s - Backup complete \n" % refinedTime)
    #
    transcript.close()
    #
    sys.exit(1)
    
    
if(__name__ == '__main__'):
    #
    main()
