# Testataan Test_suttu.py funktioiden toiminnot 

# Modulien ja kirjastojen lataukset
import  suttu

# Testataan syötettä
def test_kysy_henkilotiedot(monkeypatch):
    syote = "mika vainio"

    # Korvataan pythonin sisäinen 
    monkeypatch.setattr("builtins.input", lambda _: syote)

    assert suttu.kysy_henkilotiedot() == "mika vainio"

def test_toteamus(capsys):
    suttu.toteamus()
    naytto, virhe = capsys.readouterr()
    assert naytto == "Kyllä se siitä, herra presidentti"
    assert virhe == ""