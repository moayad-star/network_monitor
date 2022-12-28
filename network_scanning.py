try:
    # Color
    R = "\033[;31;m" #Red 
    G = "\033[;32;m" #Green
    B = "\033[;34;m" #Blue
    Y = "\033[;33;m" #Yellow
    W = "\033[;0;m"  #White
    
    # Module
    from os import system as UX # os >> system
    from time import strftime,sleep # time >> strftime,sleep
    try:
        import requests
    except ModuleNotFoundError:
        print(f"{G}Download Module 'requests' ....{W}")
        UX("pip install requests && clear")
        import requests
    try:
        import readline
    except ModuleNotFoundError:
        print(f"{G}Download Module 'readline' ....{W}"
        UX("pkg i readline* && clear")
        
    # value
    try:
        your_router_ip = input("Enter your router ip [ex: 192.168.1.1]\n>>> ")
        requests.get("http://"+your_router_ip,timeout=5)
    except (requests.exceptions.InvalidURL,requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        print(f"""
    {R}Unexpected error :/ \n
    {G}Tips \n 
    {Y}+{B} Check your internet connection \n
    {Y}+{B} check your IP input correctly \n
        """)
        exit()
    list_ips = []
    
    # start scan
    while True:
        UX(f"nmap -sn {your_router_ip}/24 | grep 'for {your_router_ip[0:4]}' > wifi.txt")
        with open("wifi.txt","r") as IPs:
            IPs = IPs.readlines()
        for ip in IPs:
            if ip not in list_ips:
                list_ips.append(ip)
                print(f"{W}>>> {Y}{ip[ip.index('for')+3:-1]} \t{W}[{G}CONNECT{W}] \t{W}[{B}Total:{G}{len(list_ips)}{W}] \t{B}TIME: {Y}{strftime('%H:%M:%S')}{W}")
        for ip in list_ips:
            if ip not in IPs:
                list_ips.remove(ip)
                print(f"{W}>>> {Y}{ip[ip.index('for')+3:-1]} \t{W}[{R}DISCONNECT{W}] \t{W}[{B}Total:{R}{len(list_ips)}{W}] \t{B}TIME: {Y}{strftime('%H:%M:%S')}{W}")
except (KeyboardInterrupt,EOFError):
    print(f"""
    {Y} User:{R} CTRL + C \n
    {Y} User stop the operation \n 
    {R} Exit ...
    """)
    UX("rm wifi.txt")
