import subprocess
import random

import sys

if ("--help" in sys.argv):
    print("""
    - If you choose 1, write mac address
    - If you choose 2, we use random mac address.
    - You write ifconfig in Linux, Linux say eth0 or wlan0 mac address. 
    Then, macchanger say what do you prefer the interface; You write.
    Warning!! : If you are operating on kali linux or different linux without an wifi card,
    your internet connection may be lost.
    For example : If you are using eth0 network, your internet connection will be disconnected. """)
    sys.exit()


print("Dear user,")
print("Warning!! : If you are operating on kali linux or diffrent linux without an wifi card, your internet connection may be lost.")

while True:
    try:
        print("-------------------")
        print("1-) Write Mac Address\n2-) Random Mac Address")
        print("-------------------")
        mac_address = input("Choose process : ")

    except:
        print("Pls, choose 1 or 2!")
        continue
    else:
        break



print("-------------------")
print("wlan0\neth0")
print("-------------------")
interface = str(raw_input("Write interface : "))

r1 = str(random.randint(0,10))
r2 = str(random.randint(0,10))

if mac_address == 1:
    write_mac_address = str(raw_input("Write Mac : "))
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",write_mac_address])
    subprocess.call(["ifconfig",interface,"up"])
    print("mac changed")

elif mac_address == 2:
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether","00:"+r1+r2+":"+r1+r2+":"+r1+r2+":"+"ba:"+r1+r2])
    subprocess.call(["ifconfig",interface,"up"])
    print("mac changed")

else:
    print("You didn't make the right choice")

