

"""
Library for manipulating ROS Names. See U{http://ros.org/wiki/Names}.
"""

import os
import sys

#TODO: why are these here?
MSG_EXT = '.msg'
SRV_EXT = '.srv'

SEP = '/'
GLOBALNS = '/'
PRIV_NAME = '~'
REMAP = ":="
ANYTYPE = '*'

if sys.hexversion > 0x03000000: #Python3
    def isstring(s):
        return isinstance(s, str) #Python 3.x
else:
    def isstring(s):
        """
        Small helper version to check an object is a string in a way that works
        for both Python 2 and 3
        """
        return isinstance(s, basestring) #Python 2.x



def load_mappings(argv):
    """
    Load name mappings encoded in command-line arguments. This will filter
    out any parameter assignment mappings.

    @param argv: command-line arguments
    @type  argv: [str]
    @return: name->name remappings. 
    @rtype: dict {str: str}
    """    
    mappings = {}
    for arg in argv:
        if REMAP in arg:
            try:
                src, dst = [x.strip() for x in arg.split(REMAP)]
                if src and dst:

                    if len(src) > 1 and src[0] == '_' and src[1] != '_':
                        #ignore parameter assignment mappings
                        pass
                    else:
                        mappings[src] = dst
            except:
                #TODO: remove
                sys.stderr.write("ERROR: Invalid remapping argument '%s'\n"%arg)
    return mappings


