import os,sys,time,requests,random
#127.255.255.255

ip1 = random.randint(1,127)
ip2 = random.randint(1,255)
ip3 = random.randint(1,255)
ip4 = random.randint(1,255)
s = open("vuln.txt" , "a")
def ss():
    ip1 = random.randint(1,127)
    ip2 = random.randint(1,255)
    ip3 = random.randint(1,255)
    ip4 = random.randint(1,255)
    loop(ip1, ip2, ip3, ip4)

def loop(ip11, ip22, ip33, ip44):
    x = 1
    s.write(f"root:root:{ip11}.{ip22}.{ip33}.{ip44}\n")
    ss()

loop(ip1, ip2, ip3 , ip4)