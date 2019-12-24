from ActionHandler import ACTION_OF, ACTION_HELP

class Arguments:

    def __init__(self, argv, actionHandlers):
        # default set to action help
        self.action_name = ACTION_HELP
        self.action_name = None
        if len(argv) > 1:
            _second_arg = argv[1]
            if _second_arg in actionHandlers:
                self.action_name = _second_arg
            else:
                self.action_name = ACTION_OF
        
        if len(argv) > 2:
            self.app_name = argv[2]
