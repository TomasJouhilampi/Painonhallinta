# Tässä modulissa määritellään luokat painon hallinta sovellukseen

# Modulien ja kirjastojen sovellukset


# Henkilö luokka

class ClassName(object):
    "yliluokka kaikille henkilötyypeille"
    def __init__(self, etunimi, sukunimi, pituus, paino, ika, sukupuoli):

        self.etumimi = etunimi
        self.sukunimi = sukunimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli

    def painoindeksi(self):
        bmi = self.paino / (self.pituus / 100) ** 2
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

class classname(object):
    ""docstring for classname""


if __name__ == "__name__":
    MikaV = henkilo("Mika", "Vainio", 171, 71, 59, 1)
    print("henkilö painaa" MikaV.paino)


    MikaV.painoindeksi()

    MikaV2 = Aikuinen("Mika", "Vainio", 171, 74, 59, 1, 70)
    print (MikaV2.etunimi, "painoindeksi", MikaV2.painoindeksi())
    print (MikaV2.etunimi, "rasvaprosentti", MikaV2.rasvaprosentti())
    
