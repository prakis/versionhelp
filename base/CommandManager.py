import subprocess as sp, shlex

class CommandManager:
    def __init__(self):
        self.commands = []
    
    def add_command(self, cmd):
        self.commands.append(cmd)
    
    def execute_all_commands(self, argv):
        _results = {}
        for cmd in self.commands:
            _val = cmd.execute(argv)
            _results[_val] = _val

        print ""
        for _res in _results:
            if _res:
                print _results[_res]


class Command:
    def __init__(self, variation):
        self.variation = variation
        self.err = None
        self.results = ""
    
    def execute(self, argv):
        _app_name = ""
        if len(argv) > 1:
            _app_name = argv[2]
        _cmd_args = shlex.split( _app_name + "  " + self.variation )
        #print "$>", _cmd_args
        try:
            sp_res = sp.Popen(_cmd_args, stdout=sp.PIPE, stderr=sp.PIPE)
            self.out, self.err = sp_res.communicate()
            if(bool(self.out) and not bool(self.err)):
                return self.out 
            #print "err->", bool(self.err), self.err
        except OSError as e:
            return _app_name + " not found \n"

