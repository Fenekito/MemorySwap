from colorama import Fore, init
from time import sleep

def __main__():
    init()
    print("            _____    _____   _   _   ____  _______  _    _  _____   _   _   ____    ____    __     _____  _____  _____  _       ____  ")
    sleep(0.1)
    print("     /\    |  __ \  / ____| | \ | | / __ \|__   __|| |  | ||  __ \ | \ | | / __ \  |___ \  /  \   / ____||_   _|/ ____|| |     / __ \ ")
    sleep(0.1)
    print("    /  \   | |  | || (___   |  \| || |  | |  | |   | |  | || |__) ||  \| || |  | |   __) || () | | |       | | | |     | |    | |  | |")
    sleep(0.1)
    print("   / /\ \  | |  | | \___ \  | . ` || |  | |  | |   | |  | ||  _  / | . ` || |  | |  |__ <  \__/  | |       | | | |     | |    | |  | |")
    sleep(0.1)
    print("  / ____ \ | |__| | ____) | | |\  || |__| |  | |   | |__| || | \ \ | |\  || |__| |  ___) |       | |____  _| |_| |____ | |____| |__| |")
    sleep(0.1)
    print(" /_/    \_\|_____/ |_____/  |_| \_| \____/   |_|    \____/ |_|  \_\|_| \_| \____/  |____/         \_____||_____|\_____||______|\____/ ")
    sleep(0.1)
    print(f"{Fore.WHITE}┌──────────────────────────────────────────────────────────────────────────────┐")
    print(f"{Fore.WHITE}│                                                                              │")
    print(f"{Fore.GREEN}│Digite um número para usar como valor de partição, ou Digite C para prosseguir│")
    print(f"{Fore.WHITE}│                                                                              │")
    print(f"{Fore.WHITE}└──────────────────────────────────────────────────────────────────────────────┘")
    x = input()
    nums = list()
    positions = list()
    while(x != "c"):
        if x.isdigit():
            nums.append(int(x))
        x = input()
    x = ""
    choices = ["best", "worst", "first"]
    print(f"{Fore.WHITE}┌────────────────────────────────────────────────────────────────────────────────────────────┐")
    print(f"{Fore.WHITE}│                                                                                            │")
    print(f"{Fore.GREEN}│Digite um número para usar como valores para inserir na partição ou digite c para prosseguir│")
    print(f"{Fore.WHITE}│                                                                                            │")
    print(f"{Fore.WHITE}└────────────────────────────────────────────────────────────────────────────────────────────┘")
    
    while(x != "c"):
        if x.isdigit():
            positions.append(int(x))
        x = input()
    x = ""

    while(x.lower() not in choices):
        print(f"{Fore.WHITE}┌────────────────────────────────────────────────┐")
        print(f"{Fore.WHITE}│                                                │")
        print(f"{Fore.GREEN}│Escolha entre o best-fit, worst-fit, e first-fit│")
        print(f"{Fore.WHITE}│                                                │")
        print(f"{Fore.WHITE}└────────────────────────────────────────────────┘")
        x = input()
    result = x.lower()
    match result:
        case "best":
            swapBest(nums, positions)
        case "worst":
            swapWorst(nums, positions)
        case "first":
            swapFirst(nums, positions)


def swapFirst(arr, pos):
    attempts = 0

    toFill = []
    while (len(toFill) < len(arr)):
        for i in range(len(arr)):
            if pos[i] <= arr[i] and not pos[i] in toFill:
                toFill.append(pos[i])
        attempt += 1
        if attempt > 10:
            print(f"{Fore.RED}Não há espaço disponível")
            quit()

    for i in range(len(arr)):
        print(f"{Fore.YELLOW}{arr[i]}kb: {toFill[i]}kb")
def swapWorst(arr, pos):
    attempts = 0

    toFill = []
    arr.sort(reverse=True)
    while (len(toFill) < len(arr)):
        for i in range(len(arr)):
            if pos[i] <= arr[i] and not pos[i] in toFill:
                toFill.append(pos[i])
        attempts += 1
        if attempts > 10:
            print(f"{Fore.RED}Não há espaço disponível")
            quit()

    for i in range(len(arr)):
        print(f"{Fore.YELLOW}{arr[i]}kb: {toFill[i]}kb")

def swapBest(arr, pos):
    attempts = 0

    toFill = []
    arr.sort()
    pos.sort()
    while(len(toFill) < len(arr)):
        for i in range(len(arr)):
            if pos[i] <= arr[i] and not pos[i] in toFill:
                toFill.append(pos[i])
        attempts += 1
        if attempts > 10:
            print(f"{Fore.RED}Não há espaço disponível")
            quit()

    for i in range(len(arr)):
        print(f"\t{Fore.YELLOW}│{arr[i]}kb: {toFill[i]}kb|")

if __name__ == '__main__':
    __main__()