import sublime
import sublime_plugin
import re
import os
from datetime import datetime
import subprocess


class GetReleaseDateCommand(sublime_plugin.TextCommand):
	def dateToEnglish(self,date):
		return date.replace("Januari","January")\
			.replace("Februari","February")\
			.replace("Maart","March")\
			.replace("Mei","May")\
			.replace("Juni","June")\
			.replace("Juli","July")\
			.replace("Augustus","August")\
			.replace("Oktober","Octob")

	def parseDate(self,date):
		date = date.rstrip().title()
		print(date)
		date = self.dateToEnglish(date)
		try:
			today = datetime.strptime(date,"%d %B %Y")
			formatted = today.strftime("[%Y-%m-%d]: ")
			return formatted
		except Exception as e:
			return

	def searchDate(self,title):
		command = "python 'C:\\Users\\cockxle\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\getReleaseDateOfGameOrMovie.py' '"+title+"'"
		# command = "python --version"
		# output = os.popen(command).read()
		CREATE_NO_WINDOW = 0x08000000
		proc = subprocess.Popen(['python', 'C:\\Users\\cockxle\\AppData\\Roaming\\Sublime Text 3\\Packages\\User\\getReleaseDateOfGameOrMovie.py',  title], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,creationflags=CREATE_NO_WINDOW)
		return proc.communicate()[0].decode("utf-8")
		
	def run(self, edit):
		line = self.view.substr(self.view.line(self.view.sel()[0]))
		line = line.replace("*"," ")
		cleanLine = line.lstrip().rstrip()
		releaseDate = self.searchDate(cleanLine)
		parsedDate = self.parseDate(releaseDate)
		print(parsedDate)
		selection = self.view.sel()
		self.view.insert(edit, selection[0].begin(),parsedDate)
		