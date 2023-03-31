from os import system
import requests
try:
    try:
        test_connect = str(requests.get("http://www.github.com/moayad-star/network_monitor"))
        if test_connect == "<Response [404]>":
            exit("\033[;41;mSorry, the project does not exist\033[;40;m\n\033[;41;mit may have been deleted :(      \033[;40;m")
        if test_connect == "<Response [200]>":
            print("\033[;42;mConnection status: good\033[;40;m")
    except (requests.exceptions.ConnectTimeout,requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
        exit("\033[;41;mYou are offline !\033[;40;m")
    print("\nUpdates are being downloading...\n\n")
    system("apt upgrade -y ; cd .. ; rm -rif network_monitor ; git clone https://github.com/moayad-star/network_monitor.git")
    print("\033[;42;mUpdated successfully\033[;40;m")
except KeyboardInterrupt:
    exit("\nExit...")
