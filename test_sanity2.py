# Sanity2-modulin testit

# Modulin lataus
import sanity2

# RAJA-ARVOTARKASTUSTEN TESTIT

# Arvo rajojen sisällä, virhekoodi 0, virhesanoma Arvo OK
def test_rajatarkistus_oikein():
    assert sanity2.rajatarkistus(100, 20, 300) == [0, 'Arvo OK'] 

# Arvo alle alarajan, virhekoodi 1, virhesanoma Arvo on alle alarajan (20)
def test_rajatarkastus_alle():
    assert sanity2.rajatarkistus(10, 20, 300) == [1,'Arvo on alle alarajan (20)']
    
# Arvo yli ylärajan, virhekoodi 2, virhesanoma Arvo on yli ylärajanrajan (300)
def test_rajatarkastus_yli():
    assert sanity2.rajatarkistus(350, 20, 300) == [2,'Arvo on yli ylärajan (300)']

# LIUKULUKUMUUNNOS TESTIT

