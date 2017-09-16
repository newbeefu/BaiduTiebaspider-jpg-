# -*- coding : UTF-8 -*-
# little log program
# time   :2017-09-14 20:20:33
# author : fu 
import sys
import datetime
import os
import string

str_ok = ' is ok.'
str_false = ' is false.'
str_already = ' is already.'
str_finish = ' is finished.'
f = open('log','a')

class iLoveLog:
	"""
	value  state
	0      already
	1      ok           ok will not write into file 
	2      false
	3      finished
	"""
	def __init__(self,path):
		f.write('\n\n'+self.GetTime()+' : now begin to log \t\t\t\t   the path is  '+ path + '\n')
	
	def GetTime(self):
		now = datetime.datetime.now()
		nowtime = now.strftime('%Y-%m-%d %H:%M:%S')
		return nowtime
	def clear(self):
		ff = open('log','w')
		ff.close()

	def log(self,value,obeject):
		"""
		value  state
		0      already
		1      ok           ok will not write into file 
		2      false
		3      finished
		4      other thing
		"""
		# f = open('log','w+')
		f.write(self.GetTime()+' :  ')
		if value == 1 : 
			return
		if value == 0 :
			f.write(obeject+str_already+'\n')
		if value == 2 :
			f.write(obeject+str_false+'\n')
		if value == 3 :
			f.write(obeject+str_finish+'\n')
		if value == 4 :
			f.write(obeject+'\n')