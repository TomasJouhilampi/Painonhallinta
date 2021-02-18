# Testataan merkkijonoa numeroarvo
numeroarvo = '123.45'

# Etsitään desimaalipisteen paikka merkkijonosta (.)
pilkunpaikka = numeroarvo.find('.')
print(pilkunpaikka)

# Pilkotaan merkkijono pisteen kohdalta
osat = numeroarvo.split('.')

# Selvitetään len-funktiolla montako osaa tuli: 1 pilkku -> 2 osaa. Jos enemmän osia -> virhe
print(osat, 'osia on', len(osat), 'kpl')

# Tietotyyppi on split-metodin ansiosta nyt merkkijonon sijaan lista,
# jossa ei ole isnumeric-metodia. Siksi muutetaan alkiot merkkijonoiksi
kokonaisosa = str(osat[0])
desimaaliosa = str(osat[1])

# Tarkistetaan ovatko merkkijonojen kirjaimet numeroita
print('Kokonaisosa numeerinen', kokonaisosa.isnumeric())
print('Desimaaliosa numeerinen', desimaaliosa.isnumeric())