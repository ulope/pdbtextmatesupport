from os.path import exists
from os import system

def mate(self):
    frame, lineno = self.stack[self.curindex]
    filename = self.canonic(frame.f_code.co_filename)
    if exists(filename):
        tm_url = 'txmt://open?url=file://%s&line=%d&column=2' % (filename, lineno)
        osa_cmd = 'tell application "TextMate" to get url "%s"' % tm_url
        system('osascript -e \'%s\'' % osa_cmd)

def preloop(self):
    mate(self)

def precmd(self, line):
    mate(self)
    return line
