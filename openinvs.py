import sublime, sublime_plugin, os, subprocess

class OpenInVsCommand(sublime_plugin.TextCommand):
    def run( self, edit, ):

        if self.view.file_name():
            command = [ "C:/Program Files (x86)/Microsoft Visual Studio 14.0/Common7/IDE/devenv.exe", "/Edit", self.view.file_name() ]
            p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            result, err = p.communicate()

            self.view.set_status('oia',result+err)
            sublime.set_timeout(self.clear,2000)

    def clear(self):
        self.view.erase_status('p4')