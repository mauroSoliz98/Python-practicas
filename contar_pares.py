#Introducir dos números por teclado, contar cuantos hay entre ellos
#contar cuantos son pares y la suma de los pares
n=int(input("Indique el número menor: "))
m=int(input("Indique el número mayor: "))
total=0;pares=0;suma_pares=0
for i in range(n,m+1): #en la suma se incluyen ambos extremos
  total+=1
  if i%2==0:
    pares+=1
    suma_pares+=i
print("Entre %i y %i hay %i números, y de ellos %i son pares." % (n,m,total,pares))
print("La suma de los pares es= ",suma_pares)
