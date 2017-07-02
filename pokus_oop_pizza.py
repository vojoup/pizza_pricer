class Pizza(object):
	def __init__(self, prumer, cena):
		self.prumer = prumer
		self.cena = cena
	def displayPizza(self):
		print('Prumer : %s\nCena : %s\n' %(self.prumer, self.cena))
	def cenaZaJednotku(self):
		cena = float(self.cena) / float(self.prumer)
		return cena

pizzy = []
pocet_pizz = int(input('Kolik pizz si prejes porovnat?\n'))
for pizza in range(pocet_pizz):
	prumer = input('Jaky ma prumer pizza cislo 1 ?\n')
	cena = input('Jaka je cena pizzy cislo 1 ?\n')
	pizzy.append(Pizza(prumer, cena))
print('')
for i in range(pocet_pizz):
	print('Pizza cislo %s' %(i + 1))
	pizzy[i].displayPizza()	