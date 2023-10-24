n : int = int(input('Enter number: '))
massiv = []

for i in range(-n,n+1):
    massiv.append(i**2)
print(massiv)