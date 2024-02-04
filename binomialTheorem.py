def fact(num):
    total = 1
    for i in range(1,num+1):
        total = total*i
    return total

def ncr(n, r):
    return (fact(n))/(fact(r)*fact(n-r))

running=True
indice = 0

while running:
    if indice <= 0:
        indice = int(input("Enter the indice: "))
    else:
        for i in range(indice+1):
            print(f"{str(ncr(indice, i))}a^{str(indice-i)}b^{str(i)}", end=" ")
            if i != indice:
                print("*", end=" ")
        running=False