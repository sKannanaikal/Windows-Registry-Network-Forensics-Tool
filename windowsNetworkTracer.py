from _winreg import *

NETWORK_DATABASE = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged"
KEY = OpenKey(HKEY_LOCAL_MACHINE, net)

def searchNetworks():
	print('[+] Searching System for networks...')
	count = 0
	while True:
		try:
			networkKey = OpenKey(KEY, str(EnumKey(KEY, count)))
			net, value, t = EnumValue(networkKey, 4)
			networkName = str(value)
			print('[+] User had joined: {network}'.format(network=networkName))
			count += 1
		except:
			break

def main():
	searchNetworks()

if __name__ == "__main__":
	main()