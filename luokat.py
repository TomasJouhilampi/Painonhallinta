<<<<<<< Updated upstream
# Tässä modulissa määritellään luokat painonhallintasovellukseen

# Modulien ja kirjastojen lataukset


# Henkilö-luokka

class Henkilo:
    """Yliluokka kaikille henkilötyypeille"""
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):
        
        self.etunimi = etunimi
=======
# Tässä modulissa määritellään luokat painon hallinta sovellukseen

# Modulien ja kirjastojen sovellukset


# Henkilö luokka

class ClassName(object):
    "yliluokka kaikille henkilötyypeille"
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):

        self.etumimi = etunimi
>>>>>>> Stashed changes
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
<<<<<<< Updated upstream
        return bmi

    @staticmethod
    def bmi(pituus, paino):
        bmi = paino / (pituus/100)**2
        return bmi

class Aikuinen(Henkilo):
    """Aliluokka aikuiselle henkilölle, perii Henkilo-luokan ominaisuudet
    ja metodit
    """
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli, tavoitepaino):
        super().__init__(etunimi, sukunimi, pituus, paino, ika, sukupuoli)
        self.tavoitepaino = tavoitepaino

    def rasvaprosentti(self):
        
        rasvaprosentti = 1.2 * self.painoindeksi() + 0.23 * self.ika - 10.8 * self.sukupuoli - 5.4
        return rasvaprosentti




if __name__ == "__main__":
    mikaV = Henkilo('Mika', 'Vainio', 171, 74, 59, 1)
    print('Henkilö painaa', mikaV.paino)

    mikaV.painoindeksi()

    mikaV2 = Aikuinen('Mika', 'Vainio', 171, 74, 59, 1, 70)
    print(mikaV2.etunimi, 'painoindeksi', mikaV2.painoindeksi())
    print(mikaV2.etunimi, 'rasvaprosentti', mikaV2.rasvaprosentti())

    # Lasketaan painoindeksi staattisella metodilla
    pituus = 171
    paino = 75

    print('Paino indeksi on ', Henkilo.bmi(pituus, paino))


    
        

=======
        print("paino indeksisi on", bmi)

class Aikuinen(Henkilo):
    ""Aliluokka aikuiselle henkilölle, perii henkilö-luokan ominaisuudet ja metodit""
    def __init__(self, etunimi, sukunimi, tavoitepaino):
        super(Classname, self). __init__()
        self.arg = arg

def rasvaprosentti(self):
    bmi = self.paino / (self.pituus / 100) **2
    rasvaprosentti = 1.2 * bmi + 0.23 * self.ika - 10.8 * self.sukupuoli
    return rasvaprosentti



if __name__ == "__name__":
    MikaV = henkilo("Mika", "Vainio", 171, 71, 59, 1)
    print("henkilö painaa" MikaV.paino)


    MikaV.painoindeksi()

    MikaV2 = Aikuinen("Mika", "Vainio", 171, 74, 59, 1, 70)
    print (MikaV2.etunimi, "painoindeksi", MikaV2.painoindeksi())
    print (MikaV2.etunimi, "rasvaprosentti", MikaV2.rasvaprosentti())
    
>>>>>>> Stashed changes
