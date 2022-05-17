import socket
import struct
import textwrap





def main():
	
	
	conn = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.ntohs(3))

	while True:
		
		
		
		raw_data, addr= conn.recvfrom(65536)

		destMac,srcMac,ethProto,data = ethernet_frame(raw_data)
		print('\nEthernet Frame')
		print('Destination : {}, Source: {}, Protocal: {}'.format(destMac,srcMac,ethProto))



def ethernet_frame(data):
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
	return (get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:])










"""
bytes_addr is iterable
mac address is broken into chunks, we need to format it now 
example:
00:50:3E:E4:4C:00
"""


def get_mac_addr(bytes_addr):
	
	bytesString = map('{:02x}'.format, bytes_addr)
	mac_addr = ':'.join(bytesString).upper()

	return(mac_addr)



main()
