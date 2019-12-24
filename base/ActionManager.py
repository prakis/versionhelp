from ActionHandler import ACTION_OF, ACTION_HELP

class ActionManager:
    def __init__(self):
        self.action_handlers = {}
        self.argv = None

    def register_action_hander(self, handler):
        """Fetch name from Action Handlers"""
        self.action_handlers[handler.name] = handler

    def process(self, argv):
        _is_handlers_empty = not bool(self.action_handlers)
        if(_is_handlers_empty):
            raise Exception('Set argv only after adding Action Handlers')
        self.argv = self.add_default_actions(argv)
        _action_name = argv[1]
        _action = self.action_handlers.get(_action_name)

        #print "AM-20:After process---", self.argv, "\n", _action
        if _action:
            _action.do_action(self.argv)

    def add_default_actions(self, argv): 

        _insert_action = None
        if len(argv) > 1:
            _second_arg = argv[1]
            if _second_arg not in self.action_handlers:
                _insert_action = ACTION_OF
        else:
            _insert_action = ACTION_HELP

        if _insert_action:
            argv.insert(1, _insert_action)
        return argv