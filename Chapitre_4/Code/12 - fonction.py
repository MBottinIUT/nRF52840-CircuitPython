def somme_entiers_consecutifs (nb1, nb2) :
	somme = 0
	for i in range(nb1, nb2+1) :
		somme = somme + i
	longueur = nb2+1-nb1
	return (longueur,somme)

n1 = 42
n2 = 55
a,b = somme_entiers_consecutifs(n1,n2)
print("La somme des {} entiers consecutifs entre {} et {} vaut : {} ".format(a,n1,n2,b))