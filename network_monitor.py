# Color
R = "\033[;31;m" #Red 
G = "\033[;32;m" #Green
B = "\033[;34;m" #Blue
Y = "\033[;33;m" #Yellow
W = "\033[;0;m"  #White
    
# Module
from os import popen as UX # os >> popen
from time import strftime,sleep # time >> strftime,sleep
from ipaddress import IPv4Address
try:
    import requests
except ModuleNotFoundError:
    print(f"[{R}WARNING{W}]Download Module '{G}requests{W}' ....")
    UX("pip install requests")
    import requests
    print(f"{W}[{G}INFO{W}] module '{G}requsts{W}' is installed")
try:
    import nmap
except ModuleNotFoundError:
    print(f"[{R}WARNING{W}]Download Module '{G}requests{W}' ....")
    UX("pip install python-nmap")
    import nmap
    print(f"{W}[{G}INFO{W}] module '{G}nmap{W}' is installed")

def main():
    try: #get IPs
        your_ip = str(UX("ifconfig | grep 'broadcast'").read()).split()[1]
        original_ips = [your_ip]
        common_subnet = ".".join(original_ips[0].split(".")[:3]) + ".0"
    except IndexError:
        exit(f"\n{R}You are offline!{W}")

    nm = nmap.PortScanner()
    list_ips = []
    
    # start scan
    print(f"\n\n\n{W}[{B}{strftime('%H:%M:%S')}{W}] [{G}CONNECT{W}] [{G}  YOU  {W}]  >>> {G}{your_ip}{W}")
    print("-"*50)
    while True:
        nm.scan(common_subnet+"-255",arguments="-sn")
        for ip in nm.all_hosts():
            if ip not in list_ips:
                list_ips.append(ip)
                print(f"{W}[{B}{strftime('%H:%M:%S')}{W}] [{G}CONNECT{W}] [{B}Total:{G}{len(list_ips)}{W}]  >>> {Y}{ip}{W}")
        for ip in list_ips:
            if ip not in nm.all_hosts():
                list_ips.remove(ip)
                print(f"{W}[{B}{strftime('%H:%M:%S')}{W}] [{R}DISCONNECT{W}] [{B}Total:{G}{len(list_ips)}{W}]  >>> {R}{ip}{W}")
        sleep(10)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt,EOFError):
        print(f"""
    {Y} User:{R} CTRL + C \n
    {Y} User stop the operation \n 
    {R} Exit ...
        """)
