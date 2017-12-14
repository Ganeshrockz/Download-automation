import httplib
import urllib2
import os
errfileptr=open("errfile.txt","w")
filepoint=1
while 1:
	url = 'file:///home/ganesh/Desktop/1/2006_1_2/'
	filepoint+=1
	if filepoint==101:
		break
	url+=str(filepoint)
	url+="/"
	url+=str(filepoint)
	url+=".html"
	response = urllib2.urlopen(url)
	if response==-1:
		print "File No found"
		continue
	webContent = response.read()

#print(webContent)

	list1=[]
	i=0
	i=webContent.find("gs_ctg2")
	while i>=0:
		if i-1>=0 and webContent[i-1]=="\"":
			list1.append(i)
		i=webContent.find("gs_ctg2",i+1)

#print(list1)

	length=len(list1)

	count=0

	val=0



	for i in range(0,length):
		foundFormat=""
		pos=int(list1[i])
		count=0
		link=""
		newpos=pos
		newpos+=10
		while 1:
			if webContent[newpos]=="]":
				break
			foundFormat+=str(webContent[newpos])
			newpos+=1
		while 1:
			if webContent[pos]=='>':
				count+=1;
			if webContent[pos]=='<' and count==1:
				break
			pos=pos-1
		pos=pos+9
		while 1:
			if webContent[pos]=="\"":
				break;
			link+=str(webContent[pos])
			pos=pos+1
		print link		
		#response1 = urllib2.urlopen(link)
		try: 
			response1 = urllib2.urlopen(link)
		except urllib2.HTTPError, e:
			#checksLogger.error('HTTPError = ' + str(e.code))
			errfileptr.write(link)
			errfileptr.write('\n')
			continue
		except urllib2.URLError, e:
			#checksLogger.error('URLError = ' + str(e.reason))
			errfileptr.write(link)
			errfileptr.write('\n')
			continue
		except httplib.HTTPException, e:
			#checksLogger.error('HTTPException')
			errfileptr.write(link)
			errfileptr.write('\n')
			continue
		except Exception:
			continue
		webContent1 = response1.read()
		name="sample"
		val=val+1
		filename=name+str(val)
		if foundFormat=="HTML":
			format1=".html"
		elif foundFormat=="PDF":
			format1=".pdf"
		filename+=format1
		directory="/home/ganesh/Desktop/1/2006_1_2/"
		directory+=str(filepoint)
		os.chdir(directory)
		fp=open(filename,"w")
		fp.write(webContent1)
		fp.close() 
errfileptr.close()		