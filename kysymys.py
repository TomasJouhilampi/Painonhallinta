# Rutiineja tietojen kysymiseen käyttäjältä

# Kirjastojen ja modulien lataukset
import sanity2

# Funktioden määrittelyt
def kysy_liukuluku(kysymys, alaraja, ylaraja):
    """Kysyy käyttäjä liukuluvun tai kokonaisluvun ja tarkistaa syötteen oikean tietotyypin ja suureden

    Args:
        kysymys (str): Käyttäjälle esitettävä kysymys
        alaraja (float): pienin sallittu arvo
        ylaraja (float): suurin sallittu arvo

    Returns:
        float: käyttäjän syöttämä arvo liukulukuna
    """
    # Kysytään käyttäjältä tietoa, kunnes saadaan järkevä arvo
    luku = 0
    tapahtui_virhe = True

    while tapahtui_virhe == True:
        vastaus_str = input(kysymys + ' ')
        tulokset = sanity2.liukuluvuksi(vastaus_str)

        # Katsotaan onko virhekoodi 0, ja tallennetaan arvo muuttujaan paino
        if tulokset[0] == 0:
            vastaus = tulokset[2]
            tarkistettu_vastaus = sanity2.rajatarkistus(vastaus, alaraja, ylaraja)
            
            # Katsotaan onko arvo sallittujen rajojen sisällä tutkimalla virhekoodia
            if tarkistettu_vastaus[0] == 0:
                tapahtui_virhe = False
                luku = vastaus

            else:
                print(tarkistettu_vastaus[1])

        # Jos virhekoodi ei ole 0, tulostetaan virheilmoitus    
        else:
            print(tulokset[1])

    return luku

if __name__ == '__main__':
    vastaus = kysy_liukuluku('Anna luku', 100, 200)
    print(vastaus)
        