import pickle
import os

'''
ICMPTYPE = {
    'type(str)':{
        'code(str)': 'description(str)''
    }
}
'''
ICMPTYPE = pickle.load(open('_static/icmpType','rb'))

'''
IP_PROTOCOL={
    i(int): 'protocol(str)'
}
'''
IP_PROTOCOL = pickle.load(open("_static/IPprotocol",'rb'))

'''
FRAME_TYPE={
    i(int): 'frame_type(str)'
}
'''
FRAME_TYPE = pickle.load(open("_static/FrameType", "rb"))

'''
ARP_OP={
    i(int): 'str'  
}
'''
ARP_OP = pickle.load(open('_static/arp_op','rb'))

'''
ARP_HARDWARE={
    int: 'str'
}
'''
ARP_HARDWARE = pickle.load(open('_static/arp_hardware','rb'))

'''
IPV6_ICMPTYPE ={
    int: str
}
'''
IPV6_ICMPTYPE = pickle.load(open('_static/IPv6_IcmpType','rb'))