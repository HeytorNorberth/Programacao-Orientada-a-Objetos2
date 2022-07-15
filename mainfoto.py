from fotografia import Fotografia, Pessoa

fotografo1 = Pessoa('Heytor', '123456789 - 01','Ed.Francisco Araujo', '999205187')
proprietario1 = Pessoa('Cristiano', '123456111 - 01','Manchester', '2222285522')
foto1 = Fotografia('walpapper cr7.jpg', fotografo1, proprietario1)
foto1.propriedades_fotografia()
print('Total de fotos: ' + str(Fotografia.get_total_fotos()))
fotografo2 = Pessoa('Romuere', '221456789 - 01', 'Picos', '55577885522')
proprietario2 = Pessoa('Copa', '773456111 - 01', 'Qatar', '4002285522')
foto2 = Fotografia('copa.png', fotografo2, proprietario2)
foto2.propriedades_fotografia()
print('Total de fotos: ' + str(Fotografia.get_total_fotos()))
