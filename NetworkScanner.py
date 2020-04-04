#/usr/bin/env python3
'''
This Tool Realted To Zaid Sabih Python Course But In Python3
Maybe There Is Some Problems I Will Try To Solve  It
Feel Free To Edit The Code It Is Yours!
I Will Explain The Code Later And Update It Cuz Have Some Things To Do First!
Have Fun!
'''
import scapy.all as scapy
import time

def Banner()
	First = "\t?? Network Scanner ??"
	Second = "?? Know who use your network ??"
	Ban = First + Second
	print(Ban)

IPRang = input("Enter IP Range: ")

time.sleep(1.3)
print("[+] Start Send Packges...\n")

def StartScan(Address):
	ARPRequest = scapy.ARP(pdst=Address)
	Broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	ARPRequestWithBrod = ARPRequest/Broadcast
	Response = scapy.arp(ARPRequestWithBrod,timeout=1,verbose=False)[0]

	print("\tIP \t\t\t MAC ADDRESS\n------------------------------------------------------")
	for Device in Response:
		print(Device[1].psrc + "\t\t" + Device[1].hwsrc)
		
Banner()
StartScan(IPRang)
