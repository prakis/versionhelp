from ActionHandler import ActionHandler, ACTION_OF
from base.CommandManager import CommandManager, Command

class VersionOfActionHandler(ActionHandler):
    def __init__(self):
        super(VersionOfActionHandler, self).__init__(ACTION_OF)

    def initialize_linux_commands(self):
        #print "---vv-linux------"
        self._posix_commands()

    def initialize_macos_commands(self):
        print "----macos----"
        self._posix_commands()

    def initialize_windows_commands(self):
        print "----windows----"

    def _posix_commands(self):
        #self.cm.add_command( linux specific commands for finding version
        self.cm.add_command(Command("-v"))
        self.cm.add_command(Command("--v"))
        self.cm.add_command(Command("-version"))
        self.cm.add_command(Command("--version"))                
