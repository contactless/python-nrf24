from nrf24 import Nrf24
nrf = Nrf24(cePin=37,spiMajor=0, spiMinor=6,channel=3,payload=15)
#~ nrf = Nrf24(cePin=55,spiMajor=0, spiMinor=7,channel=10,payload=8)
nrf.config()
nrf.setRADDR("host2")
nrf.setTADDR("host1")
print nrf.getTADDR()

nrf.printSetup()
nrf.printStatus()
while True:
    if nrf.dataReady():
        print "data: ",  nrf.getData()
        #~ break
