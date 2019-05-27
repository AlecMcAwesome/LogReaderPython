import re
import scapy


txt = input("enter path: ")

f = open(txt, "r")
cleartxt = f.read()
x = re.search("ganske", cleartxt)

def testFile(x):
  if (x):
    print("YES! We have a match!")
  else:
    print("No match")