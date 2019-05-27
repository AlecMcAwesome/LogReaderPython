import re

keywords = ["SYN", "RST, ACK"]

f = open("exampleWireshark1.txt", "r")
cleartxt = f.readlines()
#x = re.search("Source", cleartxt)

def testFile(txt):
  for line in txt:
      for word in keywords:
          if word in line:
              print(word)
              break


testFile(cleartxt)