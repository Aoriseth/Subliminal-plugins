import sublime
import sublime_plugin
from datetime import datetime


class JournalTemplateCommand(sublime_plugin.TextCommand):
	today = "Something"
	def getTime(self):
		today = datetime.today()
		formatted = today.strftime("%d %B")
		return formatted
	def run(self, edit):
		# sublime.run_command("prepare_from_template_command")
		today = self.getTime()
		line = len(today)*"="
		selection = self.view.sel()
		target = selection[0].begin()+len(today)*2+3
		target_region = sublime.Region(target,target)
		self.view.insert(edit, selection[0].begin(), str(today)+"\n"+line+"\n\n\n\n*Savour*\n*\n\n*Exercise*\n*\n\n*Gratitude*\n*\n\n*Sleep*\n*\n\n*Meditation*\n*")
		self.view.sel().clear()
		self.view.sel().add(target_region)
		