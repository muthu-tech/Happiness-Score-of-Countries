# -*- coding: utf-8 -*-
"""
Created on Thu Apr 06 13:47:11 2017

@author: Muthu
"""
from bs4 import BeautifulSoup
#import re
#import os
#import urllib2


infile = r"C:\Users\muthu\Desktop\Project\project 3\countries.htm"
outfile = open('latlong.csv','w')


soup1 = BeautifulSoup(open(infile).read())



latlon = soup1.find('div',{"itemprop":"articleBody"})
cnt = []
for row in latlon.find_all('tr'):
    col = row.find_all('td')
    print col
    cnt.append(col)
    
    
    if len(col) != 0:
        
        lat = col[1].get_text()
        lon = col[2].get_text()
        country = col[3].get_text()
        
    
        outfile.write(country.encode('utf8')+",")
        outfile.write(lat.encode('utf8')+",")
        outfile.write(lon.encode('utf8')+"\n")
 
outfile.close()
