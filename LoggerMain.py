import re
import scapy


txt = input("enter text here")

x = re.search("blue", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")