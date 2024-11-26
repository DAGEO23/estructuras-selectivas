encuentro1 = int(input("Ingrese los goles en el primer encuentro:"))
encuentro2 = int(input("Ingrese los goles en el segundo encuentro:"))
encuentro3= int(input("Ingrese los goles en el tercer encuentro:"))
encuentro4 = int(input("Ingrese los goles en el cuarto encuentro:"))
goles = encuentro1 + encuentro2 + encuentro3 + encuentro4
if goles > 10:
    promedio = goles / 4
    print("el promedio de goles anotados en los 4 encuentros es:" ,promedio)
else :
    print("No se puede calcular el promedio ")