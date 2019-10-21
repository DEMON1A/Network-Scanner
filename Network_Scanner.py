import scapy.all as scapy
import time

print("""
		   		          ?? Network Scanner ??     
	   			  	 ?? Know who use your network ??
""")

ip_rang = input("\n?Enter IP Address: ")

time.sleep(3)
print("[+]Start Send Packges...")
print("\n")

def Network_Scan(ip):
	arp = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	ARP_Req_broadcast = arp/broadcast
	answerd = scapy.srp(ARP_Req_broadcast,timeout=1,verbose=False)[0]

	print("\tIP \t\t\t MAC ADDRESS\n------------------------------------------------------")
	for item in answerd:
		print(item[1].psrc + "\t\t" + item[1].hwsrc)

Network_Scan(ip_rang)