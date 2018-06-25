#import torch.utils.data
import os
from bs4 import BeautifulSoup
import xml
import xml.etree.ElementTree as ET

#current_path = os.path.dirname(os.path.abspath(__file__))
current_path = "C:\\Users\\vlj\\Documents\\GitHub\\VisualFontRecognition\\fonts"

def get_entries():
  for path, dir, files in os.walk(current_path):
    for file in files:
      f = open(os.path.join(path, file), "r").read()
      #f = "<html><body><table>" + f + "</table></body><html>"
      soup = BeautifulSoup(f, 'html.parser')
      for tr in soup.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) == 7 and tds[5].a != None:
          yield tds[0].img['src'], tds[5].a.contents

for t in get_entries():
  print(t)
