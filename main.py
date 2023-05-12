from colorama import Fore, init
from time import sleep
from pygame import mixer

mixer.init(44100)
def __main__():
    init()
    bing = mixer.Sound("startup.mp3")
    bing.play()
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
    print(f"{Fore.GREEN}│        Digite um número para usar como valores para inserir na partição                    │")
    print(f"{Fore.GREEN}│                     ou digite C para                                                       │")
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
    for val in vals:
        added = False
        for part in parts:
            if not part["Occupied"] and val <= part["Size"]:
                part["Occupied"] = True
                part["Value"] = val
                print(part)
                added = True
                break
        if not added:
            print(f"Processo de tamanho: {val} Não pode ser adicionado a qualquer partição")

    for part in parts:
        print(f"\t{Fore.YELLOW}│{part['Size']}kb: {part['Value']}kb|")


def fitWorst(parts, vals):
    for val in vals:
        worst_fit = None
        for part in parts:
            if not part["Occupied"] and val <= part["Size"]:
                if worst_fit is None or part["Size"] > worst_fit["Size"]:
                    worst_fit = part
        if worst_fit is not None:
            worst_fit["Occupied"] = True
            worst_fit["Value"] = val
            print(worst_fit)
        else:
            print(f"Processo de tamanho: {val} Não pode ser adicionado a qualquer partição")

    for part in parts:
        print(f"\t{Fore.YELLOW}│{part['Size']}kb: {part['Value']}kb|")

    bong.play()


def fitBest(parts, vals):
    for val in vals:
        best_fit = None
        for part in parts:
            if not part["Occupied"] and val <= part["Size"]:
                if best_fit is None or part["Size"] - val < best_fit["Size"] - best_fit["Value"]:
                    best_fit = part
        if best_fit is not None:
            best_fit["Occupied"] = True
            best_fit["Value"] = val
        else:
            print(f"Processo de tamanho: {val} Não pode ser adicionado a qualquer partição")

    for part in parts:
        print(f"\t{Fore.YELLOW}│{part['Size']}kb: {part['Value']}kb|")

if __name__ == '__main__':
    __main__()