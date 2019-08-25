import sublime
import sublime_plugin
import re
import os
from datetime import datetime


class GetReleaseDateCommand(sublime_plugin.TextCommand):
	def parseDate(self,date):
		print(date)
		try:
			today = datetime.strptime(date.rstrip().title(),"%d %B %Y")
			formatted = today.strftime("%Y-%m-%d: ")
			return formatted
		except Exception as e:
			return
	def searchDate(self,title):
		print(title)
		command = "python .\getReleaseDateOfGameOrMovie.py '"+title+"'"
		print(command)
		output = os.popen(command).read()
		return output
	def run(self, edit):
		line = self.view.substr(self.view.line(self.view.sel()[0]))
		cleanLine = line.lstrip().rstrip()
		releaseDate = self.searchDate(cleanLine)
		parsedDate = self.parseDate(releaseDate)

		print(parsedDate)
		# selection = self.view.sel()
		# self.view.insert(edit, selection[0].begin(), )
		