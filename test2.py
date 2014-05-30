from nrf24 import Nrf24
nrf = Nrf24(cePin=55,spiMajor=0, spiMinor=7,channel=3,payload=15)
#~ nrf = Nrf24(cePin=37,spiMajor=0, spiMinor=6,channel=10,payload=8)

nrf.config()
nrf.setRADDR("host2")
nrf.setTADDR("host1")

nrf.printSetup()
nrf.printStatus()


while 1:
	if not nrf.isSending():
		nrf.send(map(ord,"Hello"))
		raw_input()
nrf.printSetup()
nrf.printStatus()
