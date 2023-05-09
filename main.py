def swapFirst(arr, pos):
    toFill = []
    while (len(toFill) < len(arr)):
        for i in range(len(arr)):
            if pos[i] <= arr[i] and not pos[i] in toFill:
                toFill.append(pos[i])

    for i in range(len(arr)):
        print(f"{arr[i]}kb: {toFill[i]}kb")
def swapWorst(arr, pos):
    toFill = []
    arr.sort(reverse=True)
    while (len(toFill) < len(arr)):
        for i in range(len(arr)):
            if pos[i] <= arr[i] and not pos[i] in toFill:
                toFill.append(pos[i])

    for i in range(len(arr)):
        print(f"{arr[i]}kb: {toFill[i]}kb")
def swapBest(arr, pos):
    toFill = []
    arr.sort()
    pos.sort()
    while(len(toFill) < len(arr)):
        for i in range(len(arr)):
            if pos[i] <= arr[i] and not pos[i] in toFill:
                toFill.append(pos[i])

    for i in range(len(arr)):
        print(f"{arr[i]}kb: {toFill[i]}kb")

if __name__ == '__main__':
    print("Digite um número para usar como valor de partição, digite c para prosseguir")
    x = input()
    nums = list()
    positions = list()
    while(x != "c"):
        if x.isdigit():
            nums.append(int(x))
        x = input()

    x = ""

    choices = ["best", "worst", "first"]

    print("Digite um número para usar como valores para inserir na partição ou digite c para prosseguir")
    while(x != "c"):
        if x.isdigit():
            positions.append(int(x))
        x = input()
    x = ""
    while(x.lower() not in choices):
        print("Escolha entre o best-fit, worst-fit, e first-fit")
        x = input()

    result = x.lower()
    match result:
        case "best":
            swapBest(nums, positions)
        case "worst":
            swapWorst(nums, positions)
        case "first":
            swapFirst(nums, positions)

