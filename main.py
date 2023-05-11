from colorama import Fore, init
from time import sleep


def __main__():
    init()
    print(
        "            _____    _____   _   _   ____  _______  _    _  _____   _   _   ____    ____    __     _____  _____  _____  _       ____  ")
    sleep(0.1)
    print(
        "     /\    |  __ \  / ____| | \ | | / __ \|__   __|| |  | ||  __ \ | \ | | / __ \  |___ \  /  \   / ____||_   _|/ ____|| |     / __ \ ")
    sleep(0.1)
    print(
        "    /  \   | |  | || (___   |  \| || |  | |  | |   | |  | || |__) ||  \| || |  | |   __) || () | | |       | | | |     | |    | |  | |")
    sleep(0.1)
    print(
        "   / /\ \  | |  | | \___ \  | . ` || |  | |  | |   | |  | ||  _  / | . ` || |  | |  |__ <  \__/  | |       | | | |     | |    | |  | |")
    sleep(0.1)
    print(
        "  / ____ \ | |__| | ____) | | |\  || |__| |  | |   | |__| || | \ \ | |\  || |__| |  ___) |       | |____  _| |_| |____ | |____| |__| |")
    sleep(0.1)
    print(
        " /_/    \_\|_____/ |_____/  |_| \_| \____/   |_|    \____/ |_|  \_\|_| \_| \____/  |____/         \_____||_____|\_____||______|\____/ ")
    sleep(0.1)
    print(f"{Fore.WHITE}┌──────────────────────────────────────────────────────────────────────────────┐")
    print(f"{Fore.WHITE}│                                                                              │")
    print(f"{Fore.GREEN}│Digite um número para usar como valor de partição, ou Digite C para prosseguir│")
    print(f"{Fore.WHITE}│                                                                              │")
    print(f"{Fore.WHITE}└──────────────────────────────────────────────────────────────────────────────┘")
    x = input()
    partitions = list()
    values = list()
    while (x != "c"):
        if x.isdigit():
            partitions.append({"Size" : int(x), "Occupied" : False, "Value" : 0})
        x = input()
    x = ""
    choices = ["best", "worst", "first"]
    print(f"{Fore.WHITE}┌────────────────────────────────────────────────────────────────────────────────────────────┐")
    print(f"{Fore.WHITE}│                                                                                            │")
    print(f"{Fore.GREEN}│Digite um número para usar como valores para inserir na partição ou digite c para prosseguir│")
    print(f"{Fore.WHITE}│                                                                                            │")
    print(f"{Fore.WHITE}└────────────────────────────────────────────────────────────────────────────────────────────┘")

    while (x != "c"):
        if x.isdigit():
            values.append(int(x))
        x = input()
    x = ""


    while (x.lower() not in choices):
        print(f"{Fore.WHITE}┌────────────────────────────────────────────────┐")
        print(f"{Fore.WHITE}│                                                │")
        print(f"{Fore.GREEN}│Escolha entre o best-fit, worst-fit, e first-fit│")
        print(f"{Fore.WHITE}│                                                │")
        print(f"{Fore.WHITE}└────────────────────────────────────────────────┘")
        x = input()
    result = x.lower()
    match result:
        case "best":
            fitBest(partitions, values)
        case "worst":
            fitWorst(partitions, values)
        case "first":
            fitFirst(partitions, values)


def fitFirst(parts, vals):
    for part, val in zip(parts, vals):
        if not part["Occupied"]:
            part["Occupied"] = True
            part["Value"] = val

    for part in parts:
        print(f"\t{Fore.YELLOW}│{part['Size']}kb: {part['Value']}kb|")

def fitWorst(parts, vals):
    attempts = 0

    toFill = []
    parts.sort(reverse=True)
    while (len(toFill) < len(parts)):
        for i in range(len(parts)):
            if vals[i] <= parts[i] and not vals[i] in toFill:
                toFill.append(vals[i])
        attempts += 1
        if attempts > 10:
            print(f"{Fore.RED}Não há espaço disponível")
            quit()

    for i in range(len(parts)):
        print(f"{Fore.YELLOW}{parts[i]}kb: {toFill[i]}kb")


def fitBest(parts, vals):
    attempts = 0

    toFill = []
    parts.sort()
    vals.sort()
    while (len(toFill) < len(parts)):
        for i in range(len(parts)):
            if vals[i] <= parts[i] and not vals[i] in toFill:
                toFill.append(vals[i])
        attempts += 1
        if attempts > 10:
            print(f"{Fore.RED}Não há espaço disponível")
            quit()

    for i in range(len(parts)):
        print(f"\t{Fore.YELLOW}│{parts[i]}kb: {toFill[i]}kb|")


if __name__ == '__main__':
    __main__()
