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

