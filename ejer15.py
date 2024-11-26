lado1 = int(input("igrese el lado 1 del trangulo: "))
lado2 = int(input("igrese el lado 2 del trangulo: "))
lado3 = int(input("igrese el lado 3 del trangulo: "))
if  (lado1< lado2+lado3) and (lado2< lado1+lado3) and (lado3< lado1+lado2):
    print("su triangulo es un esquilatero")
elif lado1 != lado2 and   lado2 !=lado3:
    print("su triangulo es un escaleno")