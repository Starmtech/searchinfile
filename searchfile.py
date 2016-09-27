#!/usr/bin/python
# -*- coding: utf-8 -*
###################################
#         Searchinfile            #
#      langage : Python 2.7       # 
#         date : 28/08/16         #
#          version : 1.0          #
#        auteur : devkort         #
###################################

import os
import sys
import threading

def speed(fichier):
    threads = []
    t = threading.Thread(target=search, args=(fichier,))
    threads.append(t)
    t.start()

def search(files):
   try:
      with open(files, "r") as f:
         compteur = 0
         for line in f.readlines():
            compteur += 1
            if "password" in line:
                print coloriage(files, 'blue', True)
                print "ligne numéro:", coloriage(compteur, 'green', False)
   except:
      print coloriage(files + " fichier ignoré", 'red', True)
      pass

def list(path1):
   for dossier, sous_dossiers, fichiers in os.walk(path1):
      for fichier in fichiers:
         link = os.path.join(dossier, fichier)
         search(link)

def coloriage(s, color, bold=False):
   colors = {'red': 31, 'green': 32, 'yellow': 33,
             'blue': 34}
   if os.getenv('ANSI_COLORS_DISABLED') is None and color in colors:
       if bold:
           return '\033[1m\033[%dm%s\033[0m' % (colors[color], s)
       else:
           return '\033[%dm%s\033[0m' % (colors[color], s)
   else:
       return s

print coloriage("Veuillez indiquer un emplacement ou chercher", 'blue', True)
link = raw_input()
if len(link) >= 1:
   list(link)
else:
   print coloriage("Veuillez indiquer un emplacement ou chercher", 'blue', True)
   link = raw_input()
   list(link)
