
def openPorts():
    import subprocess
    subprocess.call(["netstat", "-l"])

def diskUsage():
    import subprocess
    subprocess.call(["df", "-h"])

def nics():
    import subprocess
    subprocess.call(["ifconfig", "-a"])

def showRouteT():
    import subprocess
    subprocess.call(["netstat", "-rn"])

def tmpUsage():
    import subprocess
    subprocess.call(["du","-h", "/tmp"])

def tmpEmptyFiles():
    import subprocess
    subprocess.call(["find", "/tmp", "-type", "f", "-empty"])

def processRoot():
    import subprocess
    subprocess.call(["ps", "-u", "root"])

def menu():
    print("Please select one of the following options: " )
    print("1. show ports that are listening")
    print("2. show disk usage on your system")
    print("3. show network interfaces")
    print("4. show routing table")
    print("5. show usageof /tmp directory")
    print("6. show empty files in /tmp directory")
    print("7. show all processes of the user root")
    choice = int(input("Please select one of the above options: "))

    if choice == 1:
        openPorts()
    elif choice == 2:
        diskUsage()
    elif choice == 3:
        nics()
    elif choice == 4:
        showRouteT()
    elif choice == 5:
        tmpUsage()
    elif choice == 6:
        tmpEmptyFiles()
    elif choice == 7:
        processRoot()
    else:
        print("wrong option")

if __name__=="__main__":
    menu()
