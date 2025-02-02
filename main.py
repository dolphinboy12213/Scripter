import sys, subprocess, os
from colorama import init, Fore, Style

init() # Initialize colorama

def on_start():
    global character
    global character_lines 
    character_lines = []
    character = input("What character would you like the lines of?")


def main():
    while True:
        homescreen()
        scriptfile = file_select()
        on_start()
        with open(f"scripts/{scriptfile}", "r") as script:
            for line in script:
                if line.startswith(character):
                    character_lines.append(line)
            if not character_lines:
                print(f"Oops! No lines found for {character}")
    

def homescreen():
    while True:
        subprocess.run('clear', shell=True)
        print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "Welcome to Scripter!\n\n")
        print(Fore.GREEN + "(S)cript", end="")
        print(Fore.RED + "        (E)xit\n" + Fore.RESET)
        inp = input()
        match inp.lower():
            case "s":
                return
            case "e":
                subprocess.run('clear', shell=True)
                sys.exit()
            case _:
                continue


def file_select():
    subprocess.run('clear', shell=True)
    folder = os.listdir('./scripts')
    txtfiles = []
    for file in folder:
        if file.endswith(".txt"):
            txtfiles.append(file)
    if not txtfiles:
        raise LookupError("No '.txt' files found in /scripts/")
    while True:
        i = 1
        print(Fore.BLUE + "Choose from one the available scripts:")
        file_dictionary = {}
        for file in txtfiles:
            print(f"{i}. {file}")
            file_dictionary.update({f"{i}":f"{file}"})
            i += 1
        filenumber = input()
        if filenumber in file_dictionary:
            return file_dictionary[filenumber]
        subprocess.run('clear', shell=True)