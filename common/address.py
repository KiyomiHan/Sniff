def get_IP4_addr( IPaddr ):
    byte_str = map('{:02d}'.format, IPaddr)
    Ip_addr = '.'.join(byte_str)
    return Ip_addr

 # Returns MAC as string from bytes (ie AA:BB:CC:DD:EE:FF)
def get_mac_addr(mac_raw):
    byte_str = map('{:02x}'.format, mac_raw)
    mac_addr = ':'.join(byte_str).upper()
    return mac_addr

def get_IP6_addr(ip6_raw):
    byte_str = map('{:x}'.format, ip6_raw)
    new = []
    i = 0
    s = ''
    for item in byte_str:
        if i%2 == 1:
            s = s+item
            new.append(s)
        else:
            s = item

    Ip_addr = '.'.join(new)
    return Ip_addr

def get_raw_data(byte_str):
    string = ''
    for x in bytes(byte_str):
        string = string + '{:x}'.format(x) +" "
    return string