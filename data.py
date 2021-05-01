from yatenesturnoapp.models import Client

cli=Client(name='Las Terrazas',category='deporte',type='padel',direction='Ituzaingo 1500',description='4 canchas de blindex')
cli=Client(name='Oasis',category='deporte',type='padel',direction='Ituzaingo 300',description='2 canchas de blindex')
cli.save()
cli=Client(name='La Esperanza',category='deporte',type='padel',direction='Ituzaingo 200',description='3 canchas de blindex')
cli.save()
cli=Client(name='Racing Club',category='deporte',type='tenis',direction='Colon 2000',description='8 de polvo de ladrillo')
cli.save()
cli=Client(name='Las Canchitas',category='deporte',type='futbol 5',direction='Cerrito 2000',description='6 canchas de cesped sintetico')
cli.save()
cli=Client(name='Macola',category='gastronomia',type='restaurante',direction='Vicente Lopez 1200',description='Carnes, pastas, postres')
cli.save()
cli=Client(name='Ziro',category='gastronomia',type='heladeria',direction='Vicente Lopez 2000',description='Helados artesanales')
cli.save()
cli=Client(name='Gringo',category='gastronomia',type='restaurante',direction='Ituzaingo 1500',description='comida para llevar')
cli.save()
cli=Client(name='Mr.Jones',category='estetica',type='peluqueria',direction='Tacuari 2000',description='Peluqueria unisex')
cli.save()
cli=Client(name='Las Terrazas',category='estetica',type='peluqueria',direction='Estrada 1440',description='Peluqueria masculina')
cli.save()
cli.save()

# consultas para filtrar desde el shell
gastronomics = Client.objects.filter(category='gastronomia') #aca filtro todo por gastronomia, esto me devuelve una lista
gastronomics[0].name # me da el nombre, y asi con todos.
# si quiero filtrar por mas elementos, agrego mas comas
filtros = Client.objects.filter(category='gastronomia',type='restaurante') #aca obtengo mas cosas
 
