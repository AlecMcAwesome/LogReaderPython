import re
import socket
from collections import Counter
import sys

portPattern = re.compile(
    r'Destination Port: 21|Destination Port: 23|Destination Port: 25|Destination Port: 53|Destination Port: 80|Destination Port: 110|Destination Port: 111|Destination Port: 135|Destination Port: 139|Destination Port: 143|Destination Port: 445|Destination Port: 993|Destination Port: 995|Destination Port: 1723|Destination Port: 3306|Destination Port: 3389|Destination Port: 5900|Destination Port: 8080')
portList = set()
ipList = set()
nrIps = Counter({})

path = input("please type path to log (must be txt file): ")
try:
    log = open(path, "r")
    clearTxt = log.readlines()
    resume = open("Resume.txt", "w+")
except:
    sys.exit("something went wrong please check txt format or path")


def gatherPorts(txt):
    try:
        resume.write(
            "Resume of vulnerable destination ports from log. if logs show vulnerable ports here\n"
            "please contact administrator since there could be an incoming attack and measures must be taken \n"
            "Ports: \n")
        result = portPattern.findall(str(txt))
        for item in result:
            portList.update({item: 1})
        if len(portList) > 15:
            print(len(portList))
            print("port sweep detected, Contact adinistrator")
            for port in portList:
                resume.write("%s \n" % port)
        else:
            print("no port sweep detected")
    except:
        sys.exit("Something went wrong on Port side")


def gatherIp(txt):
    try:
        ippattern = re.compile(r"[0-9]+(?:\.[0-9]+){3}")
        result = ippattern.findall(str(txt))
        resume.write(
            "\nList of ip adresses and number of occurances. ip adresses and ports should be cross refrenced to se where \n"
            "portsweep might come from:\n \n")
        for item in result:
            ipList.add(item)
            nrIps.update({item: 1})

        resume.write("Your ip andress/adresses are the following:")
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        resume.write("\nComputer name: {0} \nIP Address: {1} \n\n".format(hostname, IPAddr))

        resume.write("\nIP addresses and number of occurrences:\n")
        for key, value in nrIps.items():
            resume.write("IP: {0}  Number of Occurrences: {1} \n".format(key, value))
    except:
        sys.exit("something went wrong on IP side")


def verdict():
    try:
        resume.write("\n \nFinal Verdict of log reader: \n\n")
        if len(portList) >= 15:
            resume.write("ports indicate sweep! contact administrator!!")
        else:
            resume.write("logs does not indicate any port sweep attack. Carry on soldier!")
    except:
        sys.exit("something went wrong on IP side")


gatherPorts(clearTxt)
gatherIp(clearTxt)
verdict()
