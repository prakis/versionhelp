#!/usr/bin/env python

import sys
from base.ActionManager import ActionManager
from base.VersionOfActionHandler import VersionOfActionHandler
from base.ActionHandler import LatestActionHandler
from base.ActionHandler import UpdateActionHandler
from base.ActionHandler import HelpActionHandler


if __name__ == '__main__':

    """ Register all ActionHandlers """
    actionMan = ActionManager()
    actionMan.register_action_hander(VersionOfActionHandler())
    actionMan.register_action_hander(LatestActionHandler())
    actionMan.register_action_hander(UpdateActionHandler())
    actionMan.register_action_hander(HelpActionHandler())
    
    actionMan.process(sys.argv)
