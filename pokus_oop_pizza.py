class Pizza(object):
	def __init__(self, prumer, cena):
		self.prumer = prumer
		self.cena = cena
	def displayPizza(self):
		print('Prumer : %s\nCena : %s\nCena za jednotku : %s\n' %(self.prumer, self.cena, self.cenaZaJednotku()))
	def cenaZaJednotku(self):
		cena = float(self.cena) / float(self.prumer)
		return cena

def display_result(ceny, pizzy):
	i = ceny.index(min(ceny))
	print('Nejlevnejsi je pizza cislo %s.\n' %(i + 1))
	print('Stoji %s kc za %s cm prumeru.\n' %(pizzy[i].cena, pizzy[i].prumer))

pizzy = []
ceny_za_jednotku = []
pocet_pizz = int(input('Kolik pizz si prejes porovnat?\n'))
for pizza in range(pocet_pizz):
	prumer = input('Jaky ma prumer pizza cislo %s ?\n' %(pizza + 1))
	cena = input('Jaka je cena pizzy cislo %s ?\n' %(pizza + 1))
	pizzy.append(Pizza(prumer, cena))
print('')
for i in range(pocet_pizz):
	print('Pizza cislo %s' %(i + 1))
	pizzy[i].displayPizza()
for i in range(pocet_pizz):
	ceny_za_jednotku.append(pizzy[i].cenaZaJednotku())
#print(min(ceny_za_jednotku))
display_result(ceny_za_jednotku, pizzy)