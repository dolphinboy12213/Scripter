import sys, subprocess, os
from colorama import init, Fore, Style


def main():
    with open("scripts/examplescript.txt", "r"):
        for line in 



def homescreen():
    while True:
        subprocess.run('clear', shell=True)
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "Welcome to Mad Libs!\n\n")
        print(Fore.GREEN + "(P)lay", end="")
        print(Fore.RED + "        (E)xit\n" + Fore.RESET)
        inp = input()
        match inp.lower():
            case "p":
                return file_select()
            case "e":
                subprocess.run('clear', shell=True)
                sys.exit()
            case _:
                continue


def file_select():
    subprocess.run('clear', shell=True)
    folder = os.listdir('./stories/templates')
    txtfiles = []
    for file in folder:
        if file.endswith(".txt"):
            txtfiles.append(file)
    if not txtfiles:
        raise LookupError("No '.txt' files found in /project/stories/templates")
    while True:
        i = 1
        print(Fore.BLUE + "Choose from one the available stories:")
        file_dictionary = {}
        for file in txtfiles:
            print(f"{i}. {file}")
            file_dictionary.update({f"{i}":f"{file}"})
            i += 1
        filenumber = input()
        if filenumber in file_dictionary:
            return file_dictionary[filenumber]
        subprocess.run('clear', shell=True)