from bs4 import BeautifulSoup
import requests
import csv
#import time
#from collections import defaultdict
#from pprint import pprint
#from gensim import corpora, models, similarities
import sys
from requests.exceptions import ConnectionError
i=0
for url in open('links.txt'):
  i = i+1
  print '---> '+str(i)
  url_r_1 = "https://en.wikipedia.org/wiki/"
  url_r = "http://en.wikipedia.org/wiki/"
  if url.startswith('https://en.wikipedia.org/wiki'):
  	title = url.replace(url_r_1,'',1)
  elif url.startswith('http://en.wikipedia.org/wiki'):
  	title = url.replace(url_r,'',1)
  else:
  	continue
  title = title.replace('\n','',1)
  title1 = title.replace('/','',10)
  url_new = "https://en.wikipedia.org/w/index.php?title="+str(title)+"&action=history&year=2009&month=-1&tagfilter="
  print url_new
  while 1:
    try:
      r = requests.get(url_new)
      soup = BeautifulSoup(r.content,"lxml")
    except ConnectionError:
      continue
    else:
      break
  #for link in soup.find_all('a',{'class':'mw-changeslist-date'}):
  #  print link.get('href')
  try:
    history =  soup.find_all('a',{'class':'mw-changeslist-date'} )[0].get('href')
  except IndexError:
    foo = open(sys.argv[1]+title1+'_2009','w')
    foo.write("None")
    foo.close
    foo = open(sys.argv[2]+title1+'_2011','w')
    foo.write("None")
    foo.close
    continue
  url_surf = "https://en.wikipedia.org"+history
  print url_surf
  while 1:
    try:
      r = requests.get(url_surf)
      soup = BeautifulSoup(r.content,"lxml")
    except ConnectionError:
      continue
    else:
      break
  foo = open(sys.argv[1]+title1+'_2009','w')
  foo1 = open('Categories','a')
  flag = 0
  flag_1 = 1
  for link in soup.find_all(["h1","h2","h3","p","li","ul","a","div"]):
    if link.get_text() == "Navigation menu":
      break
    if link.name in ("th"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
        flag = 0
    if link.name in ('a'):
      if link.get_text() == "Categories":
        flag = 1
        flag_1 = 1
        foo.write(link.get_text().encode('utf-8')+'\n')
      else:
        continue
    if link.get_text() == "v":
      break
    if link.name in ('div'):
    	if link.get_text().startswith("Hidden categories:"):
    		break
    	else:
    		continue
    if link.name in ("h1","h2"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
        flag = 0
    elif link.name in ("h3"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
        flag = 0
    elif link.name in ("li"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
      	flag_1 = 1
        for line in open('Categories'):
          if line.rstrip('\n') == link.get_text().encode('utf-8'):
            flag_1 = 0
        if flag_1 == 1:
          foo1.write(link.get_text().encode('utf-8')+'\n')
    elif link.name in ("p"):
      if flag ==1 :
        flag = 0
      for string in link:
        if string.name == 'a':
          #foo.write(string.get('href'))
          foo.write(string.get_text().encode('utf-8'))
        else:
          try:
            foo.write(string.get_text().encode('utf-8'))
          except: 
            foo.write(string.encode('utf-8'))
      foo.write('\n')
  foo.close()
  foo1.close()
  url_new = "https://en.wikipedia.org/w/index.php?title="+str(title)+"&action=history&year=2011&month=-1&tagfilter="
  while 1:
    try:
      r = requests.get(url_new)
      soup = BeautifulSoup(r.content,"lxml")
    except ConnectionError:
      continue
    else:
      break
  #for link in soup.find_all('a',{'class':'mw-changeslist-date'}):
  #  print link.get('href')
  history =  soup.find_all('a',{'class':'mw-changeslist-date'})[0].get('href')
  url_surf = "https://en.wikipedia.org"+history
  print url_surf
  while 1:
    try:
      r = requests.get(url_surf)
      soup = BeautifulSoup(r.content,"lxml")
    except ConnectionError:
      continue
    else:
      break
  foo = open(sys.argv[2]+title1+'_2011','w')
  foo1 = open('Categories','a')
  flag = 0
  flag_1 = 1
  for link in soup.find_all(["h1","h2","h3","p","li","ul","a","div"]):
    if link.get_text() == "Navigation menu":
      break
    if link.name in ("th"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
        flag = 0
    if link.name in ('a'):
      if link.get_text() == "Categories":
        flag = 1
        flag_1 = 1
        foo.write(link.get_text().encode('utf-8')+'\n')
      else:
        continue
    if link.get_text() == "v":
      break
    if link.name in ('div'):
    	if link.get_text().startswith("Hidden categories:"):
    		break
    	else:
    		continue
    if link.name in ("h1","h2"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
        flag = 0
    elif link.name in ("h3"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
        flag = 0
    elif link.name in ("li"):
      foo.write(link.get_text().encode('utf-8')+'\n')
      if flag ==1 :
      	flag_1 = 1
        for line in open('Categories'):
          if line.rstrip('\n') == link.get_text().encode('utf-8'):
            flag_1 = 0
        if flag_1 == 1:
          foo1.write(link.get_text().encode('utf-8')+'\n')
    elif link.name in ("p"):
      if flag ==1 :
        flag = 0
      for string in link:
        if string.name == 'a':
          #foo.write(string.get('href'))
          foo.write(string.get_text().encode('utf-8'))
        else:
          try:
            foo.write(string.get_text().encode('utf-8'))
          except: 
            foo.write(string.encode('utf-8'))
      foo.write('\n')
  foo.close()
  foo1.close()

  
