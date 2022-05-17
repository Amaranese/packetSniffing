# Packet Sniffing with Python  


## Ethernet Frame   

- If need to get Request to reddit
- In order to send to reddit, we need `ip`, and `return address` of my computer
- BUT before this, i need that data from my computer to my router
- http request for that meme is wrapped up in an `ip packet`
- all that is wrapped up in an `ethernet frame`
- thats how my computer talks to my router



![](https://ciscohite.files.wordpress.com/2013/05/jumbotag1.png)  
  

## Sniffer Demo Code breakdown  
   
### Ethernet frame function 
```python


# unpack ethernet frame (sync,sender,reciever...etc)
# so its going to unpack the packets 
def ethernet_frame(data):
	# struct info
	# first arg is format 
	# big-endian (BE) or little-endian (LE) the way bytes are arranged on a computer
	# 6s (6 bytes) H is small unsigned int
	# we are only looking at first 14 bytes in the packet we sniffed
	dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])

	# this func properly formats a mac addy
	# as data returned isn't human readable yet 
	# htons takes byte and make them compatible 
	# [14:] is the rest of undefined size as depends on image size
	return (get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:])

```  


## get_mac_addr function  

```python

# return formatted mac_addr i.e 00:50:3E:E4:4C:00


# return formatted mac address
# bytes_addr is iterable
# mac address is broken into chunks, we need to format it now 
# example: 00:50:3E:E4:4C:00


def get_mac_addr(bytes_addr):
	# bytes_addr is iterable
	bytesString = map('{:02x}'.format, bytes_addr)
	mac_addr = ':'.join(bytesString).upper()

	return(mac_addr)


```
