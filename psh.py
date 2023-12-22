import os
import sys
import time
import pyfiglet
from colorama import *
import colorama
import platform

class PythonShell:
    def __init__(self, verbose):
        self.stat = f"{Back.GREEN}Stat:Good"
        self.verbose = verbose

    def typ(self, string):
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char != "\n":
                time.sleep(0.001)
            else:
                time.sleep(0.05)

    def run(self):
        if self.verbose == True:
            print("LOG: PSH 1.0 (PYTHON3.11) IS STARTING NOW")
            print(f"LOG: Colorama {colorama.__version__}")
            print("LOG: PYFIGLET " + pyfiglet.__version__)
            print(f"LOG: Platform: {platform.version()}")
            # Darwin Kernel Version 18.2.0: Mon Nov 12 20:24:46 PST 2018; root:xnu-4903.231.4~2/RELEASE_X86_64

            print(f"LOG: Platform: {platform.platform()}")
            #Darwin-18.2.0-x86_64-i386-64bit
            print("LOG: New Shell is PSH 1.0")
            if platform.system() == 'Windows':
                print("WARNING: THIS IS TESTED IN DARWIN SO IT MEANS IT RUNS AT UNIX PLATFORMS.\nWARNING: IT MAY NOT WORK IN NT KERNEL(MS-DOS/Microsoft Windows(x86_64)). USE WSL TO WORK")
            
            time.sleep(5)
            os.system("clear")
            print("________")
            time.sleep(3)
            os.system("clear")
            print("________")
            time.sleep(3)
            os.system("clear")
            time.sleep(3)
            print("________")
            os.system("clear")
            
        
        self.typ(Fore.RED + Back.BLACK + pyfiglet.figlet_format("PYTHON  ", font="os2"))
        self.typ(Fore.LIGHTBLUE_EX + pyfiglet.figlet_format("SHELL  ", font="os2"))
        self.typ("for UNIX\n")

        while True:
            cmd = input(f"{Fore.GREEN} [user@{os.getcwd()}] {self.stat} {Back.BLACK} {Fore.BLUE}/=~ {Fore.WHITE}")

            if cmd == "exit":
                print("[exiting psh, running zsh/bash]")
                time.sleep(1)
                break
            elif cmd == "ls":
                os.system("ls")
                self.stat = f"{Back.GREEN}Stat:Good"
            elif cmd == "nwdr":
                dirname = input("What directory name are you gonna make: ")
                os.system("mkdir " + dirname)
                self.stat = f"{Back.GREEN}Stat:Good"
            elif cmd == "cls":
                os.system("clear")
                self.stat = f"{Back.GREEN}Stat:Good"
            elif cmd == "version":
                print(f"{Fore.BLUE} {Back.YELLOW} PYTHON Shell kernel 1.0\n{Back.BLACK}Kernel: 'Python 3.11.6 (main, Oct  2 2023, 13:45:54) [Clang 15.0.0 (clang-1500.0.40.1)] on darwin' is from. Built with GCC")
                self.stat = f"{Back.GREEN}Stat:Good"
            elif cmd == "" or cmd.isspace():
                pass
            elif cmd == "nwfl":
                fil = input("What is the filename are you gonna make: ")
                os.system("touch " + fil)
                self.stat = f"{Back.GREEN}Stat:Good"
            elif cmd.startswith("cd"):
                directory = cmd.split(" ", 1)[1]
                if directory == "~":
                    directory = os.path.expanduser("~")
                    self.stat = f"{Back.GREEN}Stat:Good"
                try:
                    os.chdir(directory)
                    self.stat = f"{Back.GREEN}Stat:Good"
                except FileNotFoundError:
                    self.typ(f"{Fore.RED} ERROR: {Fore.WHITE}Directory '{directory}' not found")
                    self.stat = f"{Back.RED}Stat:Bad"
            elif cmd == 'l':
                os.system('ls -ltr')
                self.stat = f"{Back.GREEN}Stat:Good"
            elif cmd == 'manual':
                man = input("What manual page are you gonna open: ")
                os.system("man " + man)
            elif cmd == "psh -h":
                print("Commands: exit \n manual \n l \n cd \n nwfl \n nwdr \n cls \n ls \n rm \n manual \n That's it for PSH 1.0")
            elif cmd == "rm":
                typef = input("What kind are you going to delete (File/Dir): ")

                if typef == "Dir":
                    directory = input("Enter the directory you want to delete: ")
                    try:
                        os.rmdir(directory)
                        print("Directory deleted successfully.")
                        self.stat = f"{Back.GREEN}Stat:Good"
                    except OSError as e:
                        print(f"Failed to delete directory: {e}")
                        self.stat = f"{Back.RED}Stat:Bad"

                elif typef == "File":
                    file = input("Enter the file you want to delete: ")
                    try:
                        os.remove(file)
                        print("File deleted successfully.")
                        self.stat = f"{Back.GREEN}Stat:Good"
                    except OSError as e:
                        print(f"Failed to delete file: {e}")
                        self.stat = f"{Back.RED}Stat:BAD"
            else:
                self.typ(f"{Fore.RED} ERROR: {Fore.WHITE}{cmd} not found\n")
                self.stat = f"{Back.RED}Stat:Bad"


psh = PythonShell(verbose=False)
psh.run()