import sublime
import sublime_plugin
from datetime import datetime
import os
import time


DIR = "C:\\journaldir\\"
template = '''


*Exercise*
*

*Gratitude*
*

*Sleep*
*

*Meditation*
*
'''



class JournalTemplateCommand(sublime_plugin.TextCommand):
	today = "Something"
	def getTime(self):
		today = datetime.today()
		formatted = today.strftime("%d %B")
		return formatted

	def insertText(self,edit):
		today = self.getTime()
		line = len(today)*"="
		selection = self.view.sel()
		target = selection[0].begin()+len(today)*2+3
		target_region = sublime.Region(target,target)
		self.view.insert(edit, selection[0].begin(), str(today)+"\n"+line+template)
		self.view.sel().clear()
		self.view.sel().add(target_region)

	def setCursor(self, view):
		while view.is_loading():
			print("something")
		view.run_command("goto_line", {"line": 6} )

	def createFileIfNotExists(self,edit):
		date = datetime.today()
		basedir = os.path.dirname(DIR)
		basedir = os.path.join(basedir,str(date.year))
		if not os.path.exists(basedir):
			os.mkdir(basedir)

		basedir = os.path.join(basedir,date.strftime("%Y-%m %B"))	
		if not os.path.exists(basedir):
			os.mkdir(basedir)

		day_file = date.strftime("%Y-%m-%d.md")
		basedir = os.path.join(basedir,date.strftime("%Y-%m-%d.md"))	

		today = self.getTime()
		line = len(today)*"="
		write = date.strftime("#%Y-%m-%d")+"\n\n"+str(today)+"\n"+line+"\n"+template

		if not os.path.exists(basedir):
			file = open(basedir, 'a')
			file.writelines(write)
			file.close()

		v = sublime.active_window().open_file(basedir)
		sublime.set_timeout_async(lambda: self.setCursor(v), 10)
		

	def run(self, edit):
		# sublime.run_command("prepare_from_template_command")
		self.createFileIfNotExists(edit)
		# self.insertText(edit)
		

		
