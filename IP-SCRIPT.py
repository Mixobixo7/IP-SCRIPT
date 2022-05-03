import os, time
from sys import stdout

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def green():
    GREEN = "\033[0;32m"
    stdout.write(GREEN)

def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

banner = """
 ___ ____    ____   ____ ____  ___ ____ _____ 
|_ _|  _ \  / ___| / ___|  _ \|_ _|  _ \_   _|
 | || |_) | \___ \| |   | |_) || || |_) || |  
 | ||  __/   ___) | |___|  _ < | ||  __/ | |    (por Mixobixo_7)
|___|_|     |____/ \____|_| \_\___|_|    |_|  
                                             
"""

def menu():
    red()
    print(banner)
    purple()
    time.sleep(1)
    print("1 -> Aplicar configuración")
    time.sleep(1)
    print("\n2 -> Borrar configuración")
    time.sleep(1)
    print("\n3 -> Salir")
    time.sleep(1)

    option = input("\n-->> ")

    if option == "1":
        apliconf()
    if option == "2":
        delconf()
    if option == "3":
        purple()
        os.system("clear")
        print("Hasta la próxima :D")
        time.sleep(2)
        os.system("clear")
        exit()

def apliconf():
    white()
    os.system("sudo apt install vlan net-tools kmod -y")
    print("Dependencias instaladas correctamente")
    green()
    os.system("sudo modprobe 8021q")
    print("Selecciona IP y MS para la Vlan")
    IP = input("Introduzca el CIDR: ")
    VLAN = input("Vlan: ")
    white()
    print("Debian, kali, parrot, etc... usan eth0 \nUbuntu y otros raros usan enp0s3")
    green()
    ADAPTER = input("Introduzca el nombre de la interfaz de red: ")
    os.system(f"sudo vconfig add {ADAPTER} {VLAN}")
    os.system(f"sudo ifconfig {ADAPTER}.{VLAN} {IP} up")
    time.sleep(2)
    print("Configuración aplicada correctamente")

def delconf():
    green()
    print("Selecciona VLAN para borrar")
    VLAN = input("Vlan para borrar: ")
    white()
    print("Debian, kali, parrot, etc... usan eth0 \nUbuntu y otros raros usan enp0s3")
    green()
    ADAPTER = input("Introduzca el nombre de la interfaz de red: ")
    os.system(f"sudo vconfig rem {ADAPTER}.{VLAN}")
    time.sleep(2)
    print("Configuración borrada correctamente")

if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        red()
        print()
        print("Funciona igual sin ser root ;D")
        print()
    else:
        menu()
