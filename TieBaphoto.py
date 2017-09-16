# -*- coding : UTF-8 -*-

# author :
#   time :  2017/9/13 20:50
# finished time : 2017-09-16 20:15:22
import re,os
import urllib.request
import string
from myselflog import iLoveLog


class SpidernePage:
	"""
	get photo from url
	url is the father url
	"""
	def __init__(self, url):
		"""the head url"""
		self.myurl = url
		self.urllist = []
		self.son_url = []
		self.jpgmatch = r'<img class="BDE_Image" src=".*?jpg'
		self.sonurlmatch = r'<a href="/p/.*?" title=".*?">.*?</a>'
		self.info1 = 'href="'
		self.info2 = 'title="'
	def GetPage(self,myurl):
		""" Get html page by request"""

		Log.log(0,' GetPage( '+myurl+' ) ')
		try:
			page = urllib.request.urlopen(myurl).read().decode('utf-8')
			Log.log(3,' GetPage( '+myurl+' ) ')
			return page
		except:
			Log.log(2,' GetPage( '+myurl+' ) ')

	def GetPhoto(self,page):
		"""get the url s from html page Vis re """

		Log.log(0,' GetPhoto() ')
		try:
			match = re.findall(self.jpgmatch,page,re.S)
			# match = match.replace('<','')
			Log.log(3,' GetPhoto() ')
		except:
			Log.log(2,' GetPhoto() ')
		return match
	
	def SaveUrl(self,match):
		"""take the url into urllist after refresh it """

		Log.log(0,' SaveUrl() ')
		try:
			for photo in match:
				photo = photo.replace('<img class="BDE_Image" src="','')
				if photo in self.urllist:
					pass
				else :
					self.urllist.append(photo)
			Log.log(3,' SaveUrl() ')	
		except :
			Log.log(2,' SaveUrl() ')
	
	def runonepage(self,url):
		page = self.GetPage(url)
		match = self.GetPhoto(page)
		self.SaveUrl(match)
		tmp = 0
		# return
		for url in self.urllist:
			binary_data = urllib.request.urlopen(url).read()
			tmp_file = open((str)(tmp)+'.jpg','wb')
			tmp_file.write(binary_data)
			tmp_file.close()
			tmp = tmp + 1 
		self.urllist = []
		# print('the len of urllist is ' + (str)(urllist.len()))
			
	def CreateNewFile(self,filename):
		"""
		create new file and change the workplace under the father tree
		"""
		# print()
		os.chdir(workplace)
		newplace = workplace + '\\photo'+'\\' + filename
		i = 0
		if not os.path.isdir(newplace):
			os.mkdir(newplace)
		os.chdir(newplace)
		# Log.log(4,'now the workplace is ' + newplace)

	def GetSon_url(self,page):
		Log.log(0,' GetSon_url()  ')
		try:
			match = re.findall(self.sonurlmatch,page,re.S)
			Log.log(3,' GetSon_url()  ')
		except:
			Log.log(2,' GetSon_url()  ')
		return match
	def makethematch(self,l):
		"""
		i used to write c++ , 
		i donnot really to know how to use python library
		so i used a c++ way to deal with the str
		"""
		# print('ok')
		tt  = ''
		title = ''
		try:
			pos = l.index(self.info1)
		except :
			Log.log(2,' find son url from match')
		pos = pos + 6
		while l[pos]!='"':
			tt = tt + l[pos]
			pos = pos +1 
		tt = 'https://tieba.baidu.com' + tt
		try:
			pos = l.index(self.info2)
		except :
			Log.log(2,' find son url from match')
		pos = pos + 7
		while l[pos]!='"':
			title = title + l[pos]
			pos = pos +1 
		# print(title)
		return tt , title
	def run(self,url):
		page = self.GetPage(url)
		match = self.GetSon_url(page)
		for l in match:
			try:
				tt,title = self.makethematch(l)
				print(tt) # it is to know where the program go
				if tt in self.son_url:
					pass
				else :
					self.son_url.append(tt)
				self.CreateNewFile(title)
				self.runonepage(tt)
				self.urllist = []
			except :
				Log.log(2, l)
if __name__ == '__main__':
	"""
	if you have some trouble here , it may be that you donnot create the file named "photo"
	"""
	workplace = os.getcwd()
	workplace = workplace.replace('\\','\\\\')
	Log = iLoveLog(workplace)
	url ='https://tieba.baidu.com/f?kw=%E5%A5%B3%E5%9B%BE&ie=utf-8'
	os.chdir(workplace+'\\photo')
	a = SpidernePage(url)
	a.run(url)

	"""
	there are sonething bad ;
	if you want to delete the empty , you need to di it after the funtion RUN
	and do this step

	"""
	# workplace = workplace + '\\photo'
	# for it in os.listdir(workplace):
	# 	if not os.listdir(it):
	# 		os.rmdir(it)
