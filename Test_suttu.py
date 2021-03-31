# Testataan Test_suttu.py funktioiden toiminnot 

# Modulien ja kirjastojen lataukset
import  suttu

# Testataan syötettä
def test_kysy_henkilotiedot(monkeypatch):
    syote = "mika vainio"

    # Korvataan pythonin sisäinen 
    monkeypatch.setattr("builtins.input", lambda _;syote)

    assert suttu.kysy_henkilotiedot() == "mika vainio"