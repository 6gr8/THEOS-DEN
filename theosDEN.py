import os
import os
import time
import requests
import json
import shutil
import telegram
import colorama
import os
import zipfile
import subprocess
from colorama import Fore
from color import printS,Colors

colorama.init(autoreset=True)


import ctypes
printS("[-] HEY ...", delay=0.07, color=Colors.CYAN)
def theosTW():
    os.system("clear")
    c1 = input("""
[1] - Tweak-Maker
[2] - Check-Theos
[3] - Setup-Theos
[4] - Use Terminal
[5] - Exit
""")
    if c1 == "4":
        printS("[-] Terminal .. ", delay=0.04, color=Colors.GREEN)
        os.system("clear")
        while True:
            user = input("[-] Enter Command : ")
            os.system(user)
    if c1 == "3":
        os.system("clear")
        printS("[-] Setup-Theos ..", delay=0.07, color=Colors.GREEN)
        os.system("sudo apt install bash curl sudo")
        printS("[-] Step1 Done ..", delay=0.04, color=Colors.GREEN)
        command = 'bash -c "$(curl -fsSL https://raw.githubusercontent.com/theos/theos/master/bin/install-theos)"'
        os.system(command)
    if c1 == "2":
        os.system("clear")
        cmm = subprocess.run("echo $THEOS", shell=True, stdout=subprocess.PIPE, text=True)
        output = cmm.stdout.strip()

        if os.path.exists(output):
            print("[-] THEOS FOUND :) ", output)
            input("")
            return theosTW()
        else:
            print("[X] THEOS NOT FOUND .. :(")
            input("")
            return theosTW()
    if c1 == "1":
        os.system("clear")
        printS("[-] Tweak-Maker ..", delay=0.04, color=Colors.GREEN)

        Package = input("[+] Package :") 
        Name = input("[+] Name :")
        Author = input("[+] Author :")

        os.system("clear")
        os.system("clear")
        with open('control', 'w') as c:
            c.write(f"""Package: {Package}
Name: {Name}
Version: 0.0.1
Architecture: iphoneos-arm
Description: An awesome tweak!
Maintainer: {Author}
Author: {Author}
Section: Tweaks
Depends: mobilesubstrate (>= 0.9.5000)
""")
            print("Done . control [File] ")
            time.sleep(0.1)
            os.system("clear")
        print("Wait /.. ")

        with open(f'{Name}.plist', 'w') as c:
            c.write("""
        { Filter = { Bundles = ( "com.apple.springboard" ); }; }
        """)
            print("Done . Plist [File] ")
            os.system("clear")
        print("Wait /..")

        result = subprocess.run("echo $THEOS", shell=True, stdout=subprocess.PIPE, text=True)

        output = result.stdout.strip()

        with open('Makefile', 'w') as c:
            c.write(f"""
export THEOS={output}

TARGET := iphone:clang:latest:7.0
INSTALL_TARGET_PROCESSES = SpringBoard


include $(THEOS)/makefiles/common.mk

TWEAK_NAME = {Name}

{Name}_FILES = Tweak.x
{Name}_CFLAGS = -fobjc-arc

include $(THEOS_MAKE_PATH)/tweak.mk
""")
            print("Done . Makefile [File] ")
            os.system("clear")

        print("Wait /..")
        with open('Tweak.x', 'w') as c:
            c.write("""
        // CODED BY MR DENSOR
        """)
            print("Done . Tweak.x [File] ")
            os.system("clear")
            printS("[-] DONE SiR .. ", delay=0.04, color=Colors.GREEN)
            input("")
            return theosTW()
    else:
        os.system("clear")
        printS("WHAT .. ", delay=0.04, color=Colors.GREEN)
        input("")
        return theosTW()

theosTW()
