ss = float(input("Введите систему счисления (2 или 8): "))
while ss != 2 and ss != 8:
    ss = float(input("Введите 2 или 8!!!: "))
ss = int(ss)
num = int(input("Введите число: "))
def perevod(num):
    string = ''
    while num > 0:
        string = str(num % ss) + string
        num //= ss
    return string
print(perevod(num))