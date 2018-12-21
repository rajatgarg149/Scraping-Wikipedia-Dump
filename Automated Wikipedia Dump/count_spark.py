import sys
import re


sys.argv = ['','/home/incursio/Projects/DBMS/2009/','/home/incursio/Projects/DBMS/2011/']
execfile('/home/incursio/Projects/DBMS/wiki_prac.py')

#word = sys.argv[1]

rd = []
i = 0
import glob, os
os.chdir("/home/incursio/Projects/DBMS/2009/")
for file in glob.glob("*"):
	rd.append(sc.textFile("/home/incursio/Projects/DBMS/2009/"+file))
	i += 1

rdd = sc.parallelize([''])
for j in range(0,i):
	rdd = sc.union([rdd,rd[j]])

rdd = rdd.flatMap(lambda x : x.lower().split())
#rdd.collect()


def removePunctuation(text):
	text=re.sub("[^0-9a-zA-Z ]", "" , text)
	return text

def wordCount(wordListRDD):
	return wordListRDD.map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)

rdd = (rdd.map(removePunctuation))

#rdd = rdd.filter(lambda x: x!="and" and x!="is" and x!="are" and x!="a" and x!="the" and x!="an" and x!="of" 
#	and x!="by" and x!="to" and x!="as" and x!="for" and x!="to" and x!="" and x!="in")

rdd = rdd.filter(lambda x : len(x)>4)

#top15 = wordCount(rdd).takeOrdered(15,key=lambda (k,v):-v)

#print top15


#RDD = rdd.map(lambda x : (x,1))

#output = RDD.reduceByKey(lambda x,y :x+y )

#output.lookup('')

#output = sc.parallelize([''])

def query(word):
	maxa = 0
	max_i = 0
	for j in range(0,i):
		rd[j] = rd[j].flatMap(lambda x : x.lower().split())
		rd[j] = (rd[j].map(removePunctuation))
		rd[j] = rd[j].filter(lambda x : len(x)>4)
		#RDD = rd[j].map(lambda x : (x,1))
		output = rd[j].map(lambda x : (x,1)).reduceByKey(lambda x,y :x+y )
		#print output.lookup('mining')
		if maxa < output.lookup(word):
			max_i = j
		maxa = max(maxa, output.lookup(word))
		#print max_i
		#print maxa
	os.chdir("/home/incursio/Projects/DBMS/2009/")
	k =0
	for file in glob.glob("*"):
		if k == max_i:
			print file , maxa
		k +=1

query('')
#output.lookup('')


