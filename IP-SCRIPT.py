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
        exit()

def apliconf():
    white()
    os.system("sudo apt install vlan net-tools kmod -y")
    print("Dependencias instaladas correctamente")
    green()
    os.system("sudo modprobe 8021q")
    print("Selecciona IP y MS para la Vlan\n")
    IP = input("Introduzca el CIDR: ")
    VLAN = input("Vlan: ")
    
    if os.getenv("DESKTOP_SESSION") == Ubuntu
        os.system(f"sudo vconfig add enp0s3 {VLAN}")
        os.system(f"sudo ifconfig enp0s3.{VLAN} {IP} up")
        time.sleep(2)

    else:
    #Debian, kali, parrot, o todo lo que use eth0
        os.system(f"sudo vconfig add eth0 {VLAN}")
        os.system(f"sudo ifconfig eth0.{VLAN} {IP} up")
    
        time.sleep(2)
    print("Configuración aplicada correctamente")

def delconf():
    green()
    print("Selecciona VLAN para borrar")
    VLAN = input("Vlan para borrar: ")

    if (os.getenv("DESKTOP_SESSION")) = Ubuntu
        os.system(f"sudo vconfig rem enp0s3.{VLAN}")
        time.sleep(2)
    else:   
    #Debian, kali, parrot, o todo lo que use eth0
        os.system(f"sudo vconfig rem eth0.{VLAN}")
        time.sleep(2)
    print("\n Configuración borrada correctamente")

if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        red()
        print()
        print("Funciona igual sin ser root ;D")
        print()
    else:
        menu()
