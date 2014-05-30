import random, string
from nrf24 import Nrf24
nrf = Nrf24(cePin=37,spiMajor=0, spiMinor=6,channel=3,payload=15)
#~ nrf = Nrf24(cePin=55,spiMajor=0, spiMinor=7,channel=10,payload=8)

taddr = "h-"  + "".join(random.choice(string.letters) for _ in xrange(3))
assert len(taddr) == 5

nrf.config()
nrf.setTADDR(taddr)
assert taddr == nrf.getTADDR()
print "OK"
