import os
import platform
from base.CommandManager import CommandManager, Command

'''
    Action 'of' is special and default action
    if no args passed it default action is help
'''
ACTION_OF = 'of'
ACTION_HELP = 'help'

OS_LINUX = 'Linux'
OS_MAC = 'Darwin'
OS_WIN = 'Windows'


class ActionHandler(object):
    def __init__(self, name):
        self.name = name
        self.cm = CommandManager()
        self.initialize()

    def initialize(self):
        #print "Action:", self.name, "  ", argv
        if(OS_LINUX == platform.system()):
            self.initialize_linux_commands()
        elif (OS_MAC == platform.system()):
            self.initialize_macos_commands()
        elif (OS_WIN == platform.system()):
            self.initialize_windows_commands()

    def initialize_linux_commands(self):
        pass

    def initialize_macos_commands(self):
        pass

    def initialize_windows_commands(self):
        pass

    def do_action(self, argv):
        self.cm.execute_all_commands(argv)


class HelpActionHandler(ActionHandler):
    def __init__(self):
        self.str_help = ""
        super(HelpActionHandler, self).__init__(ACTION_HELP)

    def initialize_linux_commands(self):
        self.help_msg()

    def initialize_macos_commands(self):
        self.help_msg()

    def initialize_windows_commands(self):
        self.help_msg()

    def do_action(self, argv):
        print self.str_help

    def help_msg(self):
        self.str_help = """\nTo print an app version enter 'version app-name' ex:- version firefox\n\n"""


class LatestActionHandler(ActionHandler):
    def __init__(self):
        super(LatestActionHandler, self).__init__("latest")


class UpdateActionHandler(ActionHandler):
    def __init__(self):
        super(UpdateActionHandler, self).__init__("update")
