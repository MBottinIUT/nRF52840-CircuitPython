""" Programme calculatrice"""
def traitement_operation (nb1=1, nb2=1, op='+') :
	if op == '+' :
		return (nombre1 + nombre2)
	elif op == '-' :
		return (nombre1 - nombre2)
	elif op == '*' :
		return (nombre1 * nombre2)
	elif op == '/' :
		return (float(nombre1) / nombre2)

# Programme principal
try :
	nombre1 = int(input('Quel est votre premier nombre ? '))
	nombre2 = int(input('Quel est votre second nombre ? '))
	operation = input('Quelle operation souhaitez-vous (+/-/*//) ? ')
	resultat = traitement_operation(nombre1,nombre2,operation)
	print ('{0} {1} {2} = {3}'.format(nombre1, operation, nombre2, resultat))
except ValueError :
	print ("Vous devez entrer un nombre !!")
