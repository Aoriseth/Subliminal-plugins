import sublime
import sublime_plugin
import os
from datetime import datetime


class JournalWeeklyGenerate(sublime_plugin.TextCommand):
	def formatTime(self,time):
		today = datetime.strptime(time,"%Y-%m-%d")
		formatted = today.strftime("%d %B")
		return formatted

	def createWeeklyEntry(self,entry,folder):
		weekReviewName = entry.split('.')[0]+'_WeekReview.md'
		fileToCreate = os.path.join(folder,weekReviewName)
		if not os.path.exists(fileToCreate):
			writer = open(fileToCreate,'w')
			date = self.formatTime(entry.split('.')[0])
			writer.write('# week '+date+'\n\nLowlights:\n*   \n\nHighlights:\n*   \n\nOther:\n*')

	def run(self, edit):
		file = self.view.file_name()
		folder = os.path.dirname(file)

		count = 0
		for r,d,f in os.walk(folder):
			journalEntries = list(filter(lambda entry: len(entry) == 13, f))
			total = len(journalEntries)
			for entry in journalEntries:
				print(len(entry))
				count+=1
				if count%7==0:
					self.createWeeklyEntry(entry,folder)
				if count==total:
					self.createWeeklyEntry(entry,folder)

		
		