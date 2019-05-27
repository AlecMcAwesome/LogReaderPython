import re
from collections import Counter
import socket

vulnPorts = ["21", "22", "23", "25", "53", "80", "110", "111", "135", "139", "143", "443", "445", "993", "995", "1723",
             "3306", "3389", "5900", "8080"]
portPattern = re.compile(r'Destination Port: 21|Destination Port: 23|Destination Port: 25|Destination Port: 53|Destination Port: 80|Destination Port: 110|Destination Port: 111|Destination Port: 135|Destination Port: 139|Destination Port: 143|Destination Port: 445|Destination Port: 993|Destination Port: 995|Destination Port: 1723|Destination Port: 3306|Destination Port: 3389|Destination Port: 5900|Destination Port: 8080')
ipList = []
tcpDictionary = Counter({"SYN": 0, "RST, ACK": 0, "ACK": 0})

f = open("portSweep.txt", "r")
clearTxt = f.readlines()


def synAckLookup(txt):
    keywords = ["SYN", "RST, ACK", "ACK"]
    for line in txt:
        for word in keywords:
            if word in line:
                synvar = word.count("SYN")
                if synvar == 1:
                    tcpDictionary.update({"SYN": 1})
                else:
                    break
                rstAckVar = word.count("RST")
                if rstAckVar <= 0:
                    tcpDictionary.update({"RST, ACK": 1})
                else:
                    break

                ackVar = word.count("ACK")
                if ackVar <= 0:
                    tcpDictionary.update({"ACK": 1})
                else:
                    break
def gatherPorts(txt):
    result = portPattern.findall(str(txt))
    print(result)
    if len(result) > 50:
        print(len(result))
        print("port sweep detected, Contact adinistrator")
    else:
        print("no port sweep detected")
def gatherIp(txt):
    ownName = socket.gethostbyname_ex(socket.gethostname())
    ipPattern = re.compile(r"[0-9]+(?:\.[0-9]+){3}")
    result = ipPattern.findall(str(txt))
    ipList.append(result)


gatherIp(clearTxt)
print(ipList)