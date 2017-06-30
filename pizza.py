def cena_jednotky_pizzy(prumery, ceny) :
	vysledky = []
	for pizza in range(0, pocet_pizz) :
		p = prumery[pizza]
		c = ceny[pizza]
		vysledky.append(c/p)
	return vysledky

def nejlevnejsi_pizza(vysledne_ceny) :
	return vysledne_ceny.index(min(vysledne_ceny))

pocet_pizz = int(input("Kolik ruznych cen pizzy chces porovnavat?\n"))
pizzy_prumer = []
pizzy_cena = []
cena_za_jednotku = []
for pizza in range(0, pocet_pizz) :
	#print(pizza)
	pizzy_prumer.append(int(input("Jaky prumer ma pizza " + str(pizza + 1) + '?\n')))
	pizzy_cena.append(int(input("Kolik stoji pizza " + str(pizza + 1) + '?\n')))

"""for pizza in range(0, pocet_pizz) :
	p = pizzy_prumer[pizza]
	c = pizzy_cena[pizza]
	vysledek = c / p 
	print('Pizza %s stoji %s kc za jednotku.' %((pizza + 1), vysledek))
"""
ceny_pizz_za_jednotku = cena_jednotky_pizzy(pizzy_prumer, pizzy_cena)
print('Nejlevnejsi je pizza cislo %s.' %(nejlevnejsi_pizza(ceny_pizz_za_jednotku) + 1))