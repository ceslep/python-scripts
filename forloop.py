import os
os.system("cls")
paises=["Mexico","Colombia","Brasil","Ecuador","Peru"]
""" for i in range(5):
    pais=input(f"Ingrese un pais {i}: ")
    paises.append(pais) """
print(paises[:0])
if "mexico" in paises:
    paises.remove("Mexico")
print(paises)
paises.remove(paises[0])
print(paises)
for i in range(len(paises)):
    print(paises[i])