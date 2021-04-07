# Tiedostojen luomisen ja käyttämisen kokeiluja

# Kirjastojen ja modulien lataukset
import os

# luodaan tiedosto projektin juurihakemistoon
tiedosto = open("data.txt" , "x")
tiedosto.close()

# Lisätään edelliseen tiedostoon uusi rivi
tiedosto = open("data.txt" , "a")
tiedosto.write("# Tässä tiedostossa on painoindeksitietoja")
tiedosto.close()

# Luetaan tiedosto
tiedosto = open("data.txt" , "r")
print(tiedosto.read())